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
  * houses.csv 		list of houses (Чаадаева, 11А)
  * streets.csv		list of streets (Победы 50 лет;50 Летия Победы)
  * mkd.csv			list for mergin CN data with data for gis ghkh
  
## Output
  * /houses/res-x.cvs
    Росреестр не принимает строки с повторяющимся значениям ФИАС, а программа может получить только 2-5 возможных варианты кадастрового номера.
    Поетому результат представляет набор файлов в каждом из которых ФИАС не повторяется (если он не повторяется в файле mkd)
	
  * /log/itlogh.txt
  
	
 [1]: https://rosreestr.ru/wps/PA_FCCLPGUMWPSPtalApp/ru.fccland.pgu.infoblock?param_infoblock_file_path=doc/doc_rest_online_2.doc&param_infoblock_name=cc_ib_open_data&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=/FileDownloaderController

## TODO

  * houses cn get
  * decrease error 
  * concurrent requests
  
  
  
