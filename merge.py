# -*- coding: utf-8 -*-
"""
Слияние файлов
"""

from paths import *
from os import makedirs
from os.path import isfile

#PATHF_RES = pathf_resh
#PATH_SRC = path_ghp0
#PATH_SRC = path_cn

def printres(msg, strn, street, path_res=pathf_resap):

  makedirs(path_res, exist_ok=True)
  p = 0
  
  while True:
    path_file = path_res + street + '-' + str(p) +'.csv'
	
    if isfile(path_file):
      with open(path_file, 'r') as f:
        if  any(map(lambda _ :strn not in _, f.readlines())): 
          break
          
        else:
          p += 1
          continue
		  
    else:
      break	
    
  with open(path_file, 'a') as file:
    print(msg, file=file) 

	
def mergeh(path_cn):
  """
  """
  with open(path_ghp0) as f1:
    r1 = [(line.split(';', 2)[0:2], line) for line in f1.readlines()]
	
  with open(path_cn) as f1:
    for line in f1.readlines(): 
      l = list(map(lambda x:x.strip(), line.split(';',3)))
      obj =[(i[1].strip(), l[2]) for i in r1 if l[0:2] == list(map(lambda _ : _.strip(),i[0])) and l[2] != 'None']
      if len(obj) >= 1:
        msg = ('{};{}'.format(*obj[0])) if len(obj) >= 1 else None   ##  No CN found
        street = l[0].split(',')[0].strip()
        strn = msg[::-1].split(';', 1)[1][::-1]
        printres(msg, strn, street)
  

if __name__ == '__main__':
  mergeh(path_cn)   
      
