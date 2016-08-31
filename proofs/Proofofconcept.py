# -*- coding: utf-8 -*- 

class Klass1:
  def __init__(self, param):
    self.param = param
  def function(self):
    klass2 = Klass2(self)
    return klass2

class Klass2:
  def __init__(self, Klass1):
    self.param2 = Klass1.param    
  def show_me_result(self):
    print(self.param2 * 2)
	
	
test_param = 2
test_klass1 = Klass1(test_param)
test_klass2 = test_klass1.function()
test_klass2.show_me_result()	