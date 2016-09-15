from paths import *
from pyrosreestrapi import CNRequest
from pyconcurr import pyconcur
import sys

def printres(msg, path_res=path_resp):								#dif 1
  with open(path_res, 'a') as file:
    print(msg + '\n', end='', file=file) 

	
def printlog(msg, path_log=path_itlog):								#dif 2
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
    street, house, appartment, i = *i[0].split(', '), i[1], i		#dif3
    yield  CNRequest(street_check(street, streets), house, appartment, i)	

      
def get_response(CNRequest):
  msg = ''
  req = CNRequest 
  try:  
    resp = CNRequest.get_cnresponse()
    msg = '{}; {}; {}'.format(req.address[0], req.apartment, resp.response)
    printres(msg)
  except Exception as e:
    msg = e.__class__ 
    log = '{}; {}; {}'.format(req.address[0], req.address[1], msg)
    printlog(log)

	
def make_resp_file(path_streets, path_houses, concurrency = 100): 
	
  streets = street_d(path_streets) 
	
  with open(path_ghp0) as f:									   #dif4 
    r = [line.strip().split(';') for line in f.readlines()]
    f.close()
    	
  requests = iter(r, streets)
  pyconcur(get_response, requests, concurrency)
  

if __name__ == '__main__':
  from time import time, gmtime, strftime
  from os import remove
  
  remove(path_resp) if os.path.isfile(path_resp) else None
  remove(path_itlog) if os.path.isfile(path_itlog) else None
  
  t1 = time()
  
  make_resp_file(path_streets, path_houses, concurrency = 100)
  
  
  # statistic
  dt = time() - t1
  str_dt = strftime('%M:%S', gmtime(dt))
  f = open(path_itlog, 'r')
  fails = sum(1 for line in f.readlines())
  f.close()
  f = open(path_resp, 'r')
  resps = sum(1 for line in f.readlines())
  f.close()
  print('result in {}, fails: {},  resps: {}'.format(str_dt, fails, resps))    
  
  