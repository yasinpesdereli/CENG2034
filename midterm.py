#!/usr/bin/python3

import os , sys , requests , threading

#Q1)Print PID itself

print("PID of this script is : " , os.getpid())

#Q2)If the running OS is linux ; print loadavg

print("Loadavg of the system is : " , os.getloadavg())

#Q3)Take and print 5 min loadavg value and cpu core count ,
#   if the value is near or close to the cpu core count 
#   exit script.(nproc - 5min loadavg < 1)

l1, l5, l15 = os.getloadavg()
print("5 min loadavg is : " , l5)
cpu_count = os.cpu_count()
print("Cpu count of the pc is : " , cpu_count)
result = (cpu_count) - (l5)

if result < 1 :
   sys.exit("5 min loadavg is close to cpu count \n",
	    "The difference is : " , result ,"\n",
	    "Program terminated")
else :
   print("5 min loadavg time is not close to cpu count\n",
	 "The difference is : " , result)




























