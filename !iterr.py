from paths import *
from pyrosreestrapi import CNRequest
from pyconcurr import task_queue
import sys
import time

with open(path_ghp0) as f:
  r = [line.strip().split(';') for line in f.readlines()]
  f.close()
    
def printres(msg, path_res=path_res):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_log):
  with open(path_log, 'a') as file:
    print(msg, file=file) 

def iter(data): 
  for i in data:                                                                                    
    street, house, appartment, i = *i[0].split(', '), i[1], i
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
    log = '{}; {}; {}'.format(req.address[0], req.address[1], msg)
    printlog(log)
    	
requests = iter(r)

if __name__ == '__main__':

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
  