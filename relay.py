import sys
from socket import *

if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a relay socket to listen on relay_port for new connections
relay_listener_socket = socket(AF_INET, SOCK_STREAM)

# Bind the relay's socket to relay_port
relay_listener_socket.bind(("127.0.0.1", relay_port))

# TODO: Put relay_listener_socket in LISTEN mode
relay_listener_socket.listen(1)

# TODO: Accept a connection first from client.py
client_socket, client_addr = relay_listener_socket.accept()

# TODO: Then, accept a connection from server.py
server_socket, server_addr = relay_listener_socket.accept()

# TODO: Receive data from client
data = client_socket.recv(1024)

# TODO: Forward data to server
server_socket.send(data)

# Print data that was relayed
print("Data relayed: ", data)

# TODO: Recive computed answer from server
answer = server_socket.recv(1024)

# TODO: Forward answer back to client
client_socket.send(answer)

# Print data that was relayed back
print("Data relayed back: ", data)

# TODO: Close any open sockets
relay_listener_socket.close()
server_socket.close()
client_socket.close()                                                                                                                                                                                                                            
