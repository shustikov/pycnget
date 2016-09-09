# ROSREESTR API FEATURES

  work with [rosreestr api v0.0.2][1]
                 
           |    								         houses                          mkd
    input  |       						        		 streets      resph              cnh
           |    										   |			|                 |
    module |      pyrosreestrapi   ->   pyconcurr   ->   iterh   ->   rest2csvh    ->    mergeh
           |    										   |			|                 |
    output |       										 resph		  cnh				res/houses/	
		   |
  * 
  *
  
 [1]: https://rosreestr.ru/wps/PA_FCCLPGUMWPSPtalApp/ru.fccland.pgu.infoblock?param_infoblock_file_path=doc/doc_rest_online_2.doc&param_infoblock_name=cc_ib_open_data&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=/FileDownloaderController

## TODO

  * houses cn get
  * decrease error 
  * concurrent requests
  
  
  
