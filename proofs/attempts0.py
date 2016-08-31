a=''
for i in range(-10,10):
  for attempt in range(10):
    try:
      a = 1/i
      print(a)	    
    except Exception as msg:
      a = msg.__class__
      print(msg.__class__,i)
      continue
    else: 	  	
      break
  
  else:
    print(a,i, 'not secssed')	