# -*- coding: utf-8 -*- 

"""
Получение .csv файла соответствия адрес:КН для зданий
"""
from paths import *
import json

#PATH_RES = path_cnh
#PATH_LOG = 
#PATH_SRC = path_resph

def ratefilt(resp):
  """
  returns only most relaeted CNs
  """
  arr = []
  maxrate = 0b00
  for r in resp:
    rate = 0b00
    if r['apartment'] == 'None':
      #if r['srcObject'] == '2':    rate += 0b01  
      arr += [[rate, r]]
      maxrate = rate if rate > maxrate else maxrate
    
  return [i[1] for i in arr] if len(arr) >= 1 else [{'objectCn':'None'}] 

  
def str2data(str):
  """
  python string representation of list and dicts to JSON and then to list of dicts
  """
  
  data = str.replace('"','\\"').replace("'", '"').replace('None', '"None"').strip()
  data = data.replace('\\"11"\\"', '11') #113:8113
  data = data.replace('\\"21"\\"', '21') #113:61300                Strange, need to solve
  data = data.replace('\\"31"\\"', '31') #193:88222
  return json.loads(data)

  
def printres(msg, path_res=path_cnh):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

    
def addrcn(path_resph):
  """
  create file path_resp with adress and CNs (it can be more than 1 CN for 1 apartment)
  returns amount of notes madded
  """  
  with open(path_resph) as f:
    leng = 0
    for line in f.readlines():
      i = line.split(';', 2)
      apart = i[1]
      data = str2data(i[2])
      data = ratefilt(data)	
      arr_cn = set(map(lambda dict:dict['objectCn'], data))
      d = {'add':i[0], 'apart':apart, 'data': data, 'arrcn':arr_cn}     
      print('{add}; {apart}; {}'.format(len(data), **d)) # Отладка
      [printres('{add}; {apart}; {}'.format(i, **d)) for i in list(d['arrcn'])]
      leng += 1    
    f.close()
	
  return leng

  
if __name__ == '__main__':
  from os import remove
  remove(path_cnh) if os.path.isfile(path_cnh) else None
  
  print("Обработано записей:" + str(addrcn(path_resph)), end = ', ')
  f = open(path_cnh, 'r')
  r = sum(1 for line in f.readlines())
  f.close()
  print('Найдено КН: {}'.format(r))
   
  #input("Press enter to exit")    
  
