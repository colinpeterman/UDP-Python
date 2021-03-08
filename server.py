import sys
import os
import random
import string
from socket import *

if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a TCP socket for the server
tcp_socket = socket(AF_INET, SOCK_STREAM)

# TODO: Connect this socket to the relay at relay_port
tcp_socket.connect(("localhost",relay_port))

# TODO: Receive any data relayed from the relay (i.e., any data sent by the client to the relay)
data = tcp_socket.recv(1024)

# Print debugging information
print("Data received: ", data.decode())

# Convert received number to binary
data = bin(int(data.decode()))

# TODO: Send computed answer back to relay
tcp_socket.send(data.encode())

# Print debugging information
print("Data sent back: ", data)

# TODO: Close any open sockets
tcp_socket.close()
