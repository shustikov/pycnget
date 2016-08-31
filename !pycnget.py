# -*- coding: utf-8 -*-

from pyrosreestrapi import CNRequest
from pyconcurr import task_queue
from paths import *
import sys
import time


def write_res(resp, path_res):
  arr = []
  maxrate = 0b000
  for r in resp.response:
    rate = 0b0000
    if ' пом' not in r['addressNotes']:     rate += 0b1000
    if ' ком.' not in r['addressNotes']:    rate += 0b0100
    if ' к.' not in r['addressNotes']:      rate += 0b0100
    if r['srcObject'] == 2:                 rate += 0b0010
    if ' кв' in r['addressNotes']:          rate += 0b0001
    arr += [[rate, r]]
    maxrate = rate if rate > maxrate else maxrate
  d = resp.CNRequest.address
  messages = ['{}; {}; {}; {}; {}; {}; {}; {} '.format(r[1]['addressNotes'], d[0], d[1], d[2], d[3], d[4], d[5], r[1]['objectCn']) for r in arr if r[0] == maxrate]

  with open(dir_current + 'res/' + resp.CNRequest.street + '.csv', 'a') as resf:
    [print(i, file=resf) for i in messages]
    
def write_log(resp, msg):
  d = resp.CNRequest
  
  with open(path_logok, 'a') as logf:
      print('{}; {}; {}:{}; {}; {:.2f}; {}; {}'.format(
	                                                     d.address[0],
														 d.address[1],
														 resp.status
														 resp.reason,
														 len(resp.response),
														 resp.duration,
														 msg,
														 resp.response
														 ), file = logf)

def task(CNRequest, file_log='', file_res=''):
  
    for attempt in range(10):
      try:
        msg = 'ok'
        resp = CNRequest.get_cnresponse()
        write_res(resp, path_res)
        
      except URLError as e:
        print(e,i)
        continue
        
      except Exception as e:
        msg = e.__class__     
        print(msg) 
        with open(path_lognok, 'a') as logf:
          print(CNRequest.address[0],CNRequest.address[1], msg, file=logf)
        break
        
      else:
        write_log(resp, msg)
        break

    else:     
      print(msg, 'not sucssed') 
      
    
with open(path_ghp1) as f1:
  r1 = [line.strip().split(';') for line in f1.readlines()]
  f1.close()
    
with open(path_ghp2) as f2:
  r2 = [line.strip().split(';') for line in f2.readlines()]
  f2.close()

  
iter = []
for i1 in r1[:500]:                                                                                     #предел
  i = i1[0].split(',') 
  try:  
    obj = [(i[0], i[1], i1[1], i2[:3] + i1[2:]) for i2 in r2 if i1[:2] == i2[:2]][0]                
  except Exception as msg:
    with open(path_lognok, 'a') as logf:
      print(i1, msg, file=logf)
      
  street, house, apartment, address = obj
  iter += [CNRequest(street, house, apartment, address)]  

print(len(iter)) 
iterator = (i for i in iter)   

 
stats = task_queue(task, iterator, concurrency=300)
 
while True:
    print('\rdone {done}, in work: {delayed}  '.format(**stats), sys.stdout.flush())
    if stats['delayed'] == 0:
      break
    time.sleep(0.2)  

 
input("Press enter to exit ;)")