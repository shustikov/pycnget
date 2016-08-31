def trydotask(task, arg, attempts=10):
  for attempt in range(attempts):
      try:
        msg = task(arg)
		
	  except URLError as e:
	    msg, i = e.__class__ , attempt
        continue
        
      except Exception as e:
        msg, i = e.__class__, attempt
		status = False
        break
		
      else:
	    status = True
        break
  else:
  status = False 
  
  return {'done':status, 'msg':msg, 'attempts':i}
