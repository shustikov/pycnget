# -*- coding: utf-8 -*-
"""
Пути
"""

import os
dir_current = os.path.dirname(os.path.abspath(__file__)) + '/'

file_log = 'log/log.txt'				#Общий лог
file_logok = 'log/logok.txt'            #Лог успешных попыток 
file_lognok = 'log/lognok.txt'          #Лог неудачных попыток
file_res = 'res/res.csv'                #Общий файл результата
file_resh = 'res/cnresh.csv'            #
file_ghp0 = 'src/ЖП.csv'                #
file_ghp1 = 'src/csv ЖП.csv'            #
file_ghp2 = 'src/csv ЖП2.csv'           #
file_houses = 'src/houses.csv'          #


path_log =    dir_current + file_log
path_logok =  dir_current + file_logok 
path_lognok = dir_current + file_lognok  
path_res =    dir_current + file_res
path_ghp0 =   dir_current + file_ghp0 
path_ghp1 =   dir_current + file_ghp1
path_ghp2 =   dir_current + file_ghp2
path_houses = dir_current + file_houses
path_resh =   dir_current + file_resh	


if __name__ == '__main__':
  print(path_log)
  input("Press enter to exit ;)")