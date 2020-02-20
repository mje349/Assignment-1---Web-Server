#Author: Montana Esguerra
#Date: 2/20/20
#Filename: UDPServer.py
#Description: Sample code for a webserver from the textbook

from socket import *
SERVER_PORT = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))

print('The server is ready to receive on port' + str(SERVER_PORT))

while True:
    message, clientAddress = server_socket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    server_socket.sendto(modifiedMessage.encode(), clientAddress)