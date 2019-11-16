#!/usr/bin/python3.7
import socket, sys 


#create a TCP/IP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket to the port
server_address = {'localhost', 10000}

print (sys.stder + "starting on port" + str(server_address)) 
sock.bind(server_address)  


#listening for incoming connection 
sock.listen(1)
while(True):
    #wait for a connection
    print("Wating for a connection")
    clientAddress = sock.accept()

print("Something complicated")
