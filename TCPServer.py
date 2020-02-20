#Author: Montana Esguerra
#Date: 2/20/20
#Filename: TCPServer.py
#Description: sample TCP Server program from the textbook

from socket import *

SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)

SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(1)

print('The server is ready to receive on port ' + str(SERVER_PORT))

while True:
    connection_socket, addr = SERVER_SOCKET.accept()
    sentence = connection_socket.recv(2048).decode()
    capitalizedSentence = sentence.upper()
    connection_socket.send(capitalizedSentence.encode())
    connection_socket.close()