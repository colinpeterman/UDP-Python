import sys
import os
import random
import string
import time
from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
	startTime = time.time()
	messageSend = "message number: " + str(i)
	client_socket.sendto(messageSend.encode(), ("127.0.0.1", 12000))
	client_socket.settimeout(1)	
	try:
		message, addr = client_socket.recvfrom(1024)
		finishTime = time.time()
		print("Message recieved: ", message.decode()," Time: ", (finishTime - startTime))
	
	except timeout:
		print("Request timed out")


client_socket.close()
