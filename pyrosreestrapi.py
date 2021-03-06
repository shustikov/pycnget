# -*- coding: utf-8 -*- 

"""
Запрос к api Росреестра версии 0.0.2
https://rosreestr.ru/wps/PA_FCCLPGUMWPSPtalApp/ru.fccland.pgu.infoblock?param_infoblock_file_path=doc/doc_rest_online_2.doc&param_infoblock_name=cc_ib_open_data&ru.fccland.ibmportal.spring.portlet.dispatcher.DispatcherServiceServlet.directRequest=x&ru.fccland.ibmportal.spring.portlet.handler.BeanNameParameterHandlerMapping-PATH=/FileDownloaderController
"""

import http.client
import json
import time
import sys


class CNRequest:
  """
  Тело запроса
  """
  def __init__(self, street, house, apartment, address = ''):
    self.address = address
    self.street = street
    self.house = house
    self.apartment = apartment
    self.params = json.dumps({
                                'macroRegionId' : '122000000000',
                                'regionId' : '122401000000',
								'settlementId': '122401370000', # Московский район
                                'street' : self.street,
                                'house' : self.house,
                                'apartment' : self.apartment    
                            })
           
		   
  def get_cnresponse(self):
    """
    Возвращает объект ответа
    """  
    self.response = CNResponse(self) 
    return self.response

	
class CNResponse:
  """
  Тело ответа (запрос производится при инициализации объекта)
  """
  def __init__(self, CNRequest):
    self.CNRequest = CNRequest
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    conn = http.client.HTTPConnection("rosreestr.ru:80")
    conn.request("POST", "/api/online/address/fir_objects", CNRequest.params, headers)
    start_time = time.time()
    response = conn.getresponse()   
    self.status, self.reason = response.status, response.reason
    data = response.read().decode('utf8')
    conn.close()
    self.duration = time.time() - start_time
    
    self.response = json.loads(data)
    self.address = self.response[0]['addressNotes']
    self.cn = self.response[0]['objectCn']
    self.street = self.response[0]['street']
    self.house = self.response[0]['house']
    self.apartment = self.response[0]['apartment']
 
 
  def write_log(self, file_log=''):
    """
    Для тестирования
    """
    message = '{}; {}:{}; {}; {:.2f}'.format(self.CNRequest.params, self.status, self.reason, len(self.response), self.duration)
    if file_log != '':
      with open(file_log, 'a+') as log:
        print((message), file=log)
  
    else:   
      print(message)

	  
  def write_res(self, file_res=''):
    """
    Для тестирования
    """
    messages = ['{}; {}; {}; {}'.format(r['street'], r['house'], r['apartment'], r['objectCn']) for r in self.response]
    if file_res != '':
      with open(file_res, 'a+') as res:
        [print(m, file = res) for m in messages]
    
    else:
      [print(m) for m in messages]  
 
    
if __name__ == '__main__':

  test_street, test_house, test_apartment = 'Чаадаева', '36', '11'
  test_log, test_res = 'C:/Users/ROOT/Desktop/Заливка ГИС ЖКХ/test_log.txt', 'C:/Users/ROOT/Desktop/Заливка ГИС ЖКХ/cnres.csv'
  test_request = CNRequest(test_street, test_house, test_apartment)
  
  test_response = test_request.get_cnresponse() 
  test_response.write_log(file_log)
  test_response.write_res(file_res)

  