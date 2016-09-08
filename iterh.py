"""
Module contains  response task and iterator for it 
"""

from paths import *
from pyrosreestrapi import CNRequest
from pyconcurr import pyconcur
import sys

 
#PATH_RES = path_resph
#PATH_LOG = path_itlogh
#PATH_SRC = path_houses
#PATH_STREETS = path_streets
 
def printres(msg, path_res=path_resph):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_itlogh):
  with open(path_log, 'a') as file:
    print(msg, file=file)
	
def street_d(path_streets):
  with open(path_streets, 'r') as f:
    return {l.strip().split(';')[0]:l.strip().split(';')[1] for l in f.readlines()}

def street_check(street, streets):	
  if street in streets.keys():
    return streets[street]
	
  else:
    return street 	

def iter(data, streets): 
  for i in data:                                                                                    
    street, house, appartment, i = *i[0].split(', '), '', i
    yield  CNRequest(street_check(street, streets), house, appartment, i) 
      
def get_response(CNRequest):
  msg = ''
  req = CNRequest 
  try:  
    resp = CNRequest.get_cnresponse()
    msg = '{}; {}; {}'.format(req.address[0], req.apartment, resp.response) #take address from req.address[0]
    printres(msg)
  except Exception as e:
    msg = e.__class__ 
    log = '{}; {}; {}'.format(req.address[0], '', msg)
    printlog(log)

streets = street_d(path_streets) 
  
with open(path_houses) as f:
  r = [line.strip().split(';') for line in f.readlines()]
  f.close()
    

if __name__ == '__main__':
  
  from time import time, gmtime, strftime
  from os import remove
  
  remove(path_resph) if os.path.isfile(path_resph) else None
  remove(path_itlogh) if os.path.isfile(path_itlogh) else None
  
  t1 = time()
  requests = iter(r, streets)
  
  pyconcur(get_response, requests, concurrency = 100)  
  
  # i = 0
  # while True:
    # try:
      # get_response(next(requests))
    # except StopIteration:
      # break  
    # i += 1
    # if i % 50 == 0: print(i, time() - t1)
  
  # statistic
  dt = time() - t1
  str_dt = strftime('%M:%S', gmtime(dt))
  f = open(path_itlogh, 'r')
  fails = sum(1 for line in f.readlines())
  f.close()
  f = open(path_resph, 'r')
  resps = sum(1 for line in f.readlines())
  f.close()
  print('result in {}, fails: {},  resps: {}'.format(str_dt, fails, resps)) 
  

  