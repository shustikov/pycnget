# -*- coding: utf-8 -*-
"""
Слияние файлов
"""
from paths import *
from os import makedirs

#PATHF_RES = pathf_resh
#PATH_SRC = path_mkd
#PATH_SRC = path_cnh

def printres(msg, i, path_res=pathf_resh):
  makedirs(path_res, exist_ok=True)
  with open(path_res + 'res-' + str(i) +'.csv' , 'a') as file:
    print(msg, file=file) 
	

def mergeh(path_cnh):
  """
  """
  
  with open(path_mkd) as f1:
    r1 = [(line.split(';', 1)[0], line) for line in f1.readlines()]
 
  '''
  если такой дом в пуле 0, то пишем его в пул 1 итд; пул соответствует итератору в названии файла результата, это нужно чтобы в каждом файле ФИАС был индивидуальный
  '''   	
  with open(path_cnh) as f1:
    pools = [[]]
    for line in f1.readlines(): 
	
      l = list(map(lambda x:x.strip(), line.split(';')[::2]))
      if l[1] != 'None':
        obj = [(i[1].strip(), l[1]) for i in r1 if i[0] == l[0] and l[1] != 'None']
        strn = [obj[0][0]] if len(obj) >= 1 else print(l, ':no CN')  ##  No CN found
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

if __name__ == '__main__':
  mergeh(path_cnh)   
    


