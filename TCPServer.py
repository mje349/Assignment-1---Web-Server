#Author: Montana Esguerra
#Date: 2/20/20
#Filename: TCPServer.py
#Description: sample TCP Server program from the textbook

from socket import *

SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)

#The '' is for localhost

SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(1)

print('The server is ready to receive on port ' + str(SERVER_PORT))

while True:

    #This is our "pipe"
    connection_socket, addr = SERVER_SOCKET.accept()
    #At this point, handshaking is complete

    print(addr)

    #Receive a data from the client
    sentence = connection_socket.recv(2048).decode()

    #Capitalize each character
    capitalizedSentence = sentence.upper()

    #Send it back to the client
    connection_socket.send(capitalizedSentence.encode())

    #Close the connection
    connection_socket.close()