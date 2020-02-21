#Author: Montana Esguerra
#Date: 2/20/20
#Filename: web_client2.py
#Description: Test web client program for troubleshooting

from socket import *
import sys

SERVER_NAME = 'localhost'
SERVER_PORT = 12001

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

FILE = "HelloWorld.html"

print(client_socket.getsockname())

request = FILE

client_socket.send(request.encode())

s = client_socket.recv(2048).decode()

print(s)

#f = open("HelloWorld.html", "rb")

#l = f.read(2048)

#while(l):
#    client_socket.send(l)
#    l = f.read(2048)


client_socket.close()