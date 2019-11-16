import socket
import threading


#Server Side
HOST = "0.0.0.0"
PORT =  9999
#Create a socket

def handle_client(client_socket):
    #print out what client send
    request = client_socket.recv(1024)
    print(f"[*] Received {request}")
    if request == 'GET':
      client.socket.send('')
    client_socket.send("ACK!")
    client_socket.close() 
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))
    server.listen(5)
    print(f"[*] listenning on {HOST}:{PORT}")
    while True:
        client,addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}{addr[1]}")
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:

