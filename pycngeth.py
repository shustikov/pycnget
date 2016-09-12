# -*- coding: utf-8 -*-
"""
main
"""
from time import time, gmtime, strftime
from os import remove
from paths import *
from iterh import make_resp_file
from json2csvh import addrcn

remove(path_resph) if os.path.isfile(path_resph) else None
remove(path_itlogh) if os.path.isfile(path_itlogh) else None


t1 = time()

make_resp_file(path_streets, path_houses, concurrency = 100)

dt = time() - t1
str_dt = strftime('%M:%S', gmtime(dt))
f = open(path_itlogh, 'r')
fails = sum(1 for line in f.readlines())
f.close()
f = open(path_resph, 'r')
resps = sum(1 for line in f.readlines())
f.close()
print('result in {}, fails: {},  resps: {}'.format(str_dt, fails, resps))


remove(path_cnh) if os.path.isfile(path_cnh) else None

print("Обработано записей:" + str(addrcn(path_resph)), end = ', ')
f = open(path_cnh, 'r')
r = sum(1 for line in f.readlines())
f.close()
print('Найдено КН: {}'.format(r))

mergeh(path_cnh)



