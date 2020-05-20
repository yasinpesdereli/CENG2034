#!/usr/bin/python3

import os , sys , requests , threading

#For time comparison without threads

urls = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034',
'https://github.com/caesarsalad/wow']
def response_stat(urll):
  response = requests.get(url = urll)
  	
  if response.status_code > 199 and response.status_code < 299 :
     print(urll , "status is : " , response.status_code , " so it is succesfull")
  elif response.status_code>399 and response.status_code < 600 :
     print(urll , "status is : " , response.status_code , " so it is failed")	
  else :
     print("Not in range :D")

for i in range(len(urls)) :
    response_stat(urls[i])

'''
response = requests.get(url = urls[0])
print (response.status_code)
response = requests.get(url = urls[1])
print (response.status_code)
response = requests.get(url = urls[2])
print (response.status_code)
response = requests.get(url = urls[3])
print (response.status_code)
response = requests.get(url = urls[4])
print (response.status_code)
'''
