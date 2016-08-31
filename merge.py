# -*- coding: utf-8 -*-
"""
Слияние файлов
"""

from paths import *


with open(path_ghp0) as f1:
  r1 = [line.strip().split(';') for line in f1.readlines()]
  f1.close()
    

def printres(msg, path_res=path_ghp0):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_log):
  #ЖП1-but-not-in-ЖП2
  with open(path_log, 'a') as file:
    print(msg, file=file) 
	  
iter = []
for i1 in r1:                                                                                     #предел
  try:  
    obj = [(i2[:3] + i1[2:]) for i2 in r2 if i1[:2] == i2[:2]][0]
    printres('{}; {}; {}; {}; {}; {}'.format(*obj))	
	
  except Exception as e:
    printlog('{}; {}; {}; {}'.format(i1[0], i1[1], i1, e))
      
