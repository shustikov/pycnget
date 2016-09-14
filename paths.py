# -*- coding: utf-8 -*-
"""
Пути
"""

import os
# current app dir
dc = os.path.dirname(os.path.abspath(__file__)) + '/'

# dirs
pathf_resap =   dc + 'res/temp/'
pathf_resh  =   dc + 'res/houses/'
pathf_resap =   dc + 'res/apartments/'
pathf_log	=   dc + 'log/'

# files
# sourses
path_ghp0 =   dc + 'src/ЖП.csv'          #
path_ghp1 =   dc + 'src/csv ЖП.csv'      #
path_ghp2 =   dc + 'src/csv ЖП2.csv'     #
path_streets =dc + 'src/streets.csv' 
path_houses = dc + 'src/houses.csv'      #
path_mkd  =   dc + 'src/MKD.csv'		 #
	

# logs

path_itlogh = dc + 'log/itlogh.txt'      # Лог 
path_itlog =  dc + 'log/itlog.txt'       # Лог 

# temp results

path_resph =   dc + 'res/tmp/resph.csv'	 # Файл ответов по домам
path_cnh = 	  dc + 'res/tmp/cnh.csv' 	 # Файл содержащий дома и КНы

path_resp =   dc + 'res/tmp/resp.csv'    # Файл ответов по квартирам   
path_cn =    dc + 'res/tmp/cn.csv'		 # файл квартиры и КНы	


if __name__ == '__main__':
  print(path_log)
  input("Press enter to exit ;)")
  
  