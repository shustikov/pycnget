from paths import *
from pyrosreestrapi import CNRequest
from pyconcurr import task_queue
import sys
import time
 
#PATH_RES = path_res
#PATH_LOG = path_log
#PATH_SRC = path_houses
 
def printres(msg, path_res=path_res):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_log):
  with open(path_log, 'a') as file:
    print(msg, file=file) 

def iter(data): 
  for i in data:                                                                                    
    street, house, appartment, i = *i[0].split(', '), '', i
    yield  CNRequest(street, house, appartment, i)
      
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

  requests = iter(r)

  i = 0
  while True:
    try:
    	get_response(next(requests))
    except StopIteration:
    	break  
    i += 1
    if i % 50 == 0: print(i)
  
  #stats = task_queue(get_response, requests, 5)  
  
  #while True:
  #  print('\rdone {done}, in work: {delayed}  '.format(**stats), sys.stdout.flush())
  #  if stats['delayed'] == 0:
  #    break
  #  time.sleep(0.2)  
  