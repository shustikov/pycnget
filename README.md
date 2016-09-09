# ROSREESTR API FEATURES

  work with [rosreestr api v0.0.2][1]
                 
           |    								         houses                          mkd
    input  |       						        		 streets      resph              cnh
           |    										   |			|                 |
    module |      pyrosreestrapi   ->   pyconcurr   ->   iterh   ->   json2csvh    ->    mergeh
           |    										   |			|                 |
    output |       										 resph		  cnh				res/houses/	
		   |

## Input
  * /src/houses.csv 		list of houses (Чаадаева, 11А)
  * /src/streets.csv		list of streets (Победы 50 лет;50 Летия Победы)
  * /src/mkd.csv			list for merging CN data with data for gis ghkh (Чаадаева, 11; 13; [data];...[data]; )
  
## Output
  * /houses/res-x.cvs
    Росреестр не принимает строки с повторяющимся значениям ФИАС, а программа может получить только 2-5 возможных варианты кадастрового номера дома.
    Поэтому результат представляет набор файлов в каждом из которых ФИАС не повторяется (если он не повторяется в файле mkd)
	
  * /log/itlogh.txt
    Ошибки обращения к росреестру.
	
 [1]: https://rosreestr.ru/wps/PA_FCCLPGUMWPSPtalApp/ru.fccland.pgu.infoblock?param_infoblock_file_path=doc/doc_rest_online_2.doc&param_infoblock_name=cc_ib_open_data&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=/FileDownloaderController

## PROBLEMS
  * (4/1000) TimeoutError  in itlogh - try again.
  * <json.decoder.JSONDecodeError> in itlogh - RR can`t find this address, usualy for 2 word streets. Add pair of streets to streets.csv file e.g. 
  (Жукова Маршала;Маршала Жукова)
  * (5/1000) json.decoder.JSONDecodeError in itlogh for 1 word street - need to solve.
  * (6/1000) json.decoder.JSONDecodeError in json2csvh in apartment numbers - need to solve.
  * (all) more than 1 most likely appropriate (apartment:'None') CN number for 1 object. 
  * (400/1000) RR have more than 200 objects related with this address for some houses. RR can`t return more than 200 objects
  apartment:'None' - objects may be absent in response.  
 
## TODO

  * decrease error
  
  
  
