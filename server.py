import socket
import threading


def connect_a_client(conn,add):
    print("New client has been connected")
    data = conn.recv(2048)
    print("Data recived from server is :",data)
    conn.sendall(b"Server has received your data")

HOST = "localhost"

PORT = 3000

# created  a new socket 
server_socket = socket.socket()

#bind the socket object to thehost and port

server_socket.bind((HOST,PORT))

# start  listening the new connection

server_socket.listen()

print("Server is listening on {HOST}:{PORT}")

while True:
    #wait  for  new connection
    conn,addr = server_socket.accept()
    t = threading.Thread(target=connect_a_client,args=(conn,addr))
    t.start()








