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
  maxrate = 0b00
  for r in resp:
    rate = 0b00
	if r['apartment'] == None:
	  #if ' пом' not in r['addressNotes']:     rate += 0b000000010
	  #if ' ком.' not in r['addressNotes']:    rate += 0b000000010
	  #if ' к.' not in r['addressNotes']:      rate += 0b000000010
      if r['srcObject'] == 2:                 rate += 0b01  #
	  #if ' кв'  not in r['addressNotes']:     rate += 0b000000010
      arr += [[rate, r]]
      maxrate = rate if rate > maxrate else maxrate
    
  return [i[1] for i in arr if i[0] == maxrate]

  
def str2data(str):
  """
  python string representation of list and dicts to JSON and then to list of dicts
  """  
  data = str.replace('"','\\"').replace("'", '"').replace('None', '"None"').strip()
  return json.loads(data)

  
def printres(msg, path_res=path_res):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

    
def addrcn(path_resph):
  """
  create file path_resp with adress and CNs (it can be more than 1 CN for 1 apartment)
  returns amount of notes maded
  """  
  with open(path_resp) as f:
    #r = []
    len = 0
    for line in f.readlines():
      i = line.split(';')
      apart = i[1]
      data = str2data(i[2])                                          
      data = ratefilt(data)
      arr_cn = set(map(lambda dict:dict['objectCn'], data))
      d = {'add':i[0], 'apart':apart, 'data': data, 'arrcn':arr_cn}     
      #r.append(d)
      [print('{add}; {apart}; {}'.format(i, **d)) for i in list(d['arrcn'])]
      len += 1    
    f.close()
    return len

 
  
if __name__ == '__main__':
  print("Сделано записей:" + str(addrcn(path_resp)))
   
  #input("Press enter to exit")    
  
