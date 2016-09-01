# -*- coding: utf-8 -*-
"""
Слияние файлов
"""

from paths import *

with open(path_mkd) as f1:
  r1 = [(line.split(';', 1)[0], line) for line in f1.readlines()]
  f1.close()

def printres(msg, path_res=path_res):
  with open(path_res, 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_log):
  #ЖП1-but-not-in-ЖП2
  with open(path_log, 'a') as file:
    print(msg, file=file) 

with open(path_hcn) as f1:
  for line in f1.readlines():    #предел
    l = list(map(lambda x:x.strip(), line.split(';')[::2]))
    obj = [(i[1].strip(), l[1]) for i in r1 if i[0] == l[0] and l[1] != 'None']
    printres('{};{}'.format(*obj[0])) if len(obj) >= 1 else None
    #try:  
    #   
    #   printres() 
    #   
    #except Exception as e:
    #   printlog('{}; {}; {}; {}'.format(i1[0], i1[1], i1, e))
    #  
