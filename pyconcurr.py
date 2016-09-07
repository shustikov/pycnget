"""
Module for concurrency HTTP calls.
"""
from pyrosreestrapi import CNRequest        
from concurrent.futures import ThreadPoolExecutor, Future, TimeoutError
import sys
import time
import threading

def task_queue(task, iterator, concurrency=10, on_fail=lambda _: None):
  """
  Concurrent execution of task in number of pools.
  """
  def submit():
    try:
      obj = next(iterator)
      
    except StopIteration:
      return
      
    if result.cancelled():
      return
      
    stats['delayed'] += 1
    future = executor.submit(task, obj)
    future.obj = obj
    future.add_done_callback(upload_done)

    
  def upload_done(future):
    with io_lock:
      submit()
      stats['delayed'] -= 1
      stats['done'] += 1
      
    if future.exception():
      on_fail(future.exception(), future.obj)
      
    if stats['delayed'] == 0:
      result.set_result(stats)

      
  def cleanup(_):
    with io_lock:
      executor.shutdown(wait=False)

  io_lock = threading.RLock()
  executor = ThreadPoolExecutor(concurrency)
  result = Future()
  result.stats = stats = {'done': 0, 'delayed': 0}
  result.add_done_callback(cleanup)

  with io_lock:
    for _ in range(concurrency):
      submit()

  return result

    
def retry(func, attempts=10):
  '''
  Wrap function for HTTP calls. Retries call if URLError. Raise error if all attempts falls.
  '''
  def wraper():     
    for attempt in range(attempts):
      try:
        task()
      
      except URLError as e:
        error = e
        continue
      
      except TimeoutError as e:
        error = e
        continue      
      
      else:
        break
        
    else:
      raise error
      
  return wraper 
  
  
def pyconcur(task, iterator, concurrency=10):
  """
  main
  """   
  result = task_queue(task, iterator, concurrency)
  
  try:
    while not result.done():
      try:
        result.result(.2)
        
      except TimeoutError:
        pass    
        print('\rdone {done}, in work: {delayed}  '.format(**result.stats))
        sys.stdout.flush()
          
  except KeyboardInterrupt:
    result.cancel()
    raise  

    
    
if __name__ == '__main__':
  
  test_street, test_house, test_apartment = '50', '1', '11'
  test_request = CNRequest(test_street, test_house, test_apartment)
  file_log = 'C:/Users/adm/Desktop/rosreestr/log.txt'
  file_res = 'C:/Users/adm/Desktop/rosreestr/cnres.csv'
   
  def task(CNRequest, file_log='', file_res=''):
    test_response = test_request.get_cnresponse() 
    test_response.write_log()
    test_response.write_res()
     
  iterator = ((test_request, file_log, file_res) for i in range(1)) 
  pyconcur(task, iterator, concurrency=100)
  
  
 