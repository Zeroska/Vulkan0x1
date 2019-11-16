#!/usr/bin/env python3

import socket


HOST = '127.0.0.1' #host of the server
PORT = 9999 #port of ther server you want to connect 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT)) #what is this do, create a connection to a host server
  s.sendall(b'ACK!') # What sendall does is ??
  data = s.recv(1024) #received data at the rate of 1024

print("Recived", repr(data))
#what does this call ???
