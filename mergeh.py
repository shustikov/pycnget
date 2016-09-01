# -*- coding: utf-8 -*-
"""
Слияние файлов
"""

from paths import *

with open(path_mkd) as f1:
  r1 = [(line.split(';', 1)[0], line) for line in f1.readlines()]
  f1.close()

def printres(msg, i, path_res=path_resf):
  with open(path_res + 'res-' + str(i) +'.csv' , 'a') as file:
    print(msg, file=file) 

def printlog(msg, path_log=path_log):
  #ЖП1-but-not-in-ЖП2
  with open(path_log, 'a') as file:
    print(msg, file=file) 

with open(path_hcn) as f1:
  pools = [[]]
  for line in f1.readlines():    #предел 
    l = list(map(lambda x:x.strip(), line.split(';')[::2]))
    if l[1] != 'None':
      obj = [(i[1].strip(), l[1]) for i in r1 if i[0] == l[0] and l[1] != 'None']
      strn = [obj[0][0]] if len(obj) >= 1 else print(l)
      p = 0
      while True:
        if strn not in pools[p]: 
          pools[p] += [strn]
          printres('{};{}'.format(*obj[0]), p) if len(obj) >= 1 else None
          break
        
        else:
          p += 1
          pools += [[]] if len(pools) <= p else []
          continue
    

[print(p, len(pools[p])) for p in range(len(pools))]     
    
'''
если такой дом в пуле 0, то пишем его в пул 1 итд; пул соответсвует итератеру в названии файла результата, это нужно чтобы в каждом файле ФИАС был индивидульный
'''   
    #try:  
    #   
    #   printres() 
    #   
    #except Exception as e:
    #   printlog('{}; {}; {}; {}'.format(i1[0], i1[1], i1, e))
    #  
