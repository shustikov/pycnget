# -*- coding: utf-8 -*- 

"""
Получение .csv файла соответствия адрес:КН для зданий
"""
from paths import *
import json


def ratefilt(resp):
  """
  returns only most relaeted CNs
  """
  arr = []
  maxrate = 0b00
  for r in resp:
    rate = 0b00
    if r['apartment'] == 'None':
      if r['srcObject'] == '2':    rate += 0b01  
      arr += [[rate, r]]
      maxrate = rate if rate > maxrate else maxrate
    
  return [i[1] for i in arr] if len(arr) >= 1 else [{'objectCn':'None'}] 

  
def str2data(str):
  """
  python string representation of list and dicts to JSON and then to list of dicts
  """
  str = str.replace('"11\'"', '11')   
  data = str.replace('"','\\"').replace("'", '"').replace('None', '"None"').strip()
  return json.loads(data)

  
def printres(msg, path_res=path_res):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

    
def addrcn(path_resph):
  """
  create file path_resp with adress and CNs (it can be more than 1 CN for 1 apartment)
  returns amount of notes madded
  """  
  with open(path_resph) as f:
    r = []
    leng = 0
    for line in f.readlines():
      i = line.split(';')
      apart = i[1]
      data = str2data(i[2])
      data = ratefilt(data)	
      arr_cn = set(map(lambda dict:dict['objectCn'], data))
      d = {'add':i[0], 'apart':apart, 'data': data, 'arrcn':arr_cn}     
      r.append(d)
      [printres('{add}; {apart}; {}'.format(i, **d)) for i in list(d['arrcn'])]
      leng += 1    
    f.close()
	
  return leng

  
if __name__ == '__main__':
  print("Обработано записей:" + str(addrcn(path_resph)))
   
  #input("Press enter to exit")    
  
