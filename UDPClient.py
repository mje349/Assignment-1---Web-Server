#Author: Montana Esguerra
#Date: 2/20/20
#Filename: UDPClient.py
#Description: Sample UDP Client program from the textbook

from socket import *

SERVER_NAME = 'hostname'
PORT = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
client_socket.sendto(message.encode(), (SERVER_NAME, PORT))
modifiedMessage, serverAddress = client_socket.recvfrom(2048)

print(modifiedMessage.decode())

client_socket.close()

