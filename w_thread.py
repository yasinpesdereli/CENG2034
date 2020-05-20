#!/usr/bin/python3

import os , sys , requests , threading

#Q4)Check if the links in these urls are valid (working) or not. (Hint: You can use python
#requests lib. HTTP response status code 2xx is successful. 4xx or 5xx means failed.)
#*Implement this with threads. 

urls = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034',
'https://github.com/caesarsalad/wow']


def response_stat(urll):
  response = requests.get(url = urll)
  	
  if response.status_code > 199 and response.status_code < 299 :
     print(urll , " status is : " , response.status_code , " so it is succesfull")
  elif response.status_code>399 and response.status_code < 600 :
     print(urll , " status is : " , response.status_code , " so it is failed")	
  else :
     print("Not in range :D")


thread1 = threading.Thread(target = response_stat , args = (urls[0],))
thread2 = threading.Thread(target = response_stat , args = (urls[1],))
thread3 = threading.Thread(target = response_stat , args = (urls[2],))
thread4 = threading.Thread(target = response_stat , args = (urls[3],))
thread5 = threading.Thread(target = response_stat , args = (urls[4],))


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

