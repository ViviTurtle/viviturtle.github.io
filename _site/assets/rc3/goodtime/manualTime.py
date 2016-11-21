#!/usr/bin/env python
import time
import socket
import re
import sys

timer = time.clock if sys.platform == 'win32' else time.time

#host to connect to
host="54.167.134.245"
#the port with whatever u want 
port = 5866
#creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#default alues
flag = ""
highestTime = 0
attempt= "RC3-2016-"
allowedChars = "klmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#start timer
start = timer()
#start connecction
s.connect((host, port))
#Recover 2014 bytes of response and print
data2 = s.recv(1024)
print data2
print "Attempting: " + attempt
#Send out flag
s.send(attempt + '\n')
#Read response
data2 = s.recv(1024)
#end timer
print timer()-start

#RC3-2016-itz-alw4yz-a-g00d-t1m1ng-@tt@ck
