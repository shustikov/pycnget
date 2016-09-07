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
 
def printres(msg, path_res=path_resph):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_itlogh):
  with open(path_log, 'a') as file:
    print(msg, file=file) 

def iter(data): 
  for i in data:                                                                                    
    street, house, appartment, i = *i[0].split(', '), '', i
    yield  CNRequest(street.split(' ')[0], house, appartment, i)
      
def get_response(CNRequest):
  msg = ''
  req = CNRequest 
  try:  
    resp = CNRequest.get_cnresponse()
    msg = '{}, {}; {}; {}'.format(req.street, req.house, req.apartment, resp.response)
    printres(msg)
  except Exception as e:
    msg = e.__class__ 
    log = '{}; {}; {}'.format(req.address[0], '', msg)
    printlog(log)

    
with open(path_houses) as f:
  r = [line.strip().split(';') for line in f.readlines()]
  f.close()
    

if __name__ == '__main__':
  
  from time import time, gmtime, strftime
  from os import remove
  
  remove(path_resph)
  remove(path_itlogh)
  
  t1 = time()
  requests = iter(r)
  
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
  

  