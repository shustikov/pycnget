# -*- coding: utf-8 -*- 

"""
Получение .csv файла соответствия адрес:КН
"""
from paths import *
import json


def ratefilt(resp):
  """
  returns only most relaeted CNs
  """
  arr = []
  maxrate = 0b0000
  for r in resp:
    rate = 0b0000
    if ' пом' not in r['addressNotes']:     rate += 0b1000
    if ' ком.' not in r['addressNotes']:    rate += 0b0100
    if ' к.' not in r['addressNotes']:      rate += 0b0100
    if r['srcObject'] == 1:                 rate += 0b0010
    if ' кв' in r['addressNotes']:          rate += 0b0001
    arr += [[rate, r]]
    maxrate = rate if rate > maxrate else maxrate
    
  return [i[1] for i in arr if i[0] == maxrate]

  
def str2data(str):
  """
  python string representation of list and dicts to JSON and then to list of dicts
  """  
  data = str.replace('"','\\"').replace("'", '"').replace('None', '"None"').strip()
  return json.loads(data)

  
def printres(msg, path_res=path_cn):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

    
def addrcn(path_resp):
  """
  create file path_resp with adress and CNs (it can be more than 1 CN for 1 apartment)
  returns amount of notes maded
  """  
  with open(path_resp) as f:
    leng = 0
    err = 0
    for line in f.readlines():
      try:
        i = line.split(';',2)
        apart = i[1].strip()
      
        data0 = str2data(i[2])
        data = ratefilt(data0)
        arr_cn = set(map(lambda dict:dict['objectCn'], data))
        d = {'add':i[0], 'apart':apart, 'data': data, 'arrcn':arr_cn}     
        print('{add}; {apart}; {}'.format(len(data0), **d)) if data == [{'objectCn':'None'}] else None
        [printres('{add};{apart}; {}'.format(i, **d)) for i in list(d['arrcn'])]
      except Exception as e:
        print(i, e.__class__)
        err += 1        
      leng += 1    
    f.close()
  return leng, err

 
  
if __name__ == '__main__':
  from os import remove
  remove(path_cn) if os.path.isfile(path_cn) else None
  leng, err = addrcn(path_resp)
  print("Обработано записей:" + str(leng) + ", Ошибок:" + str(err)  , end = ', ')
  f = open(path_cn, 'r')
  r = sum(1 for line in f.readlines())
  f.close()
  print('Найдено КН:{}'.format(r))

