# -*- coding: utf-8 -*-
"""
Пути
"""

import os
# current app dir
dс = os.path.dirname(os.path.abspath(__file__)) + '/'

# dirs
pathf_resap =   dc + 'res/temp/'
pathf_resh  =   dc + 'res/tmp/houses/'
pathf_resap =   dc + 'res/apartments/'
pathf_logs	=   dc + 'log/'

# files
# sourses
path_ghp0 =   dс + 'src/ЖП.csv'          #
path_ghp1 =   dс + 'src/csv ЖП.csv'      #
path_ghp2 =   dс + 'src/csv ЖП2.csv'     #
path_houses = dс + 'src/houses.csv'      #
path_resph =  dс + 'src/MKD.csv'

# logs
path_log =    dс + 'log/log.txt'		 # Общий лог
path_logok =  dс + 'log/logok.txt'       # Лог успешных попыток 
path_lognok = dс + 'log/lognok.txt'      # Лог неудачных попыток 

# temp results
path_res =    dс + 'res/res.csv'         # Общий файл результата (для тестов)

path_resh =   dс + 'res/tmp/resph.csv'	 # Файл ответов по домам
path_cnh = 	  dс + 'res/tmp/cnh.csv' 	 # Файл содержащий дома и КНы

path_resp =   dс + 'res/tmp/resp.csv'    # Файл ответов по квартирам   
path_hcn =    dс + 'res/tmp/cn.csv'		 # файл квартиры и КНы	


if __name__ == '__main__':
  print(path_log)
  input("Press enter to exit ;)")
  
  