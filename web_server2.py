#Author: Montana Esguerra
#Date: 2/20/20
#Filename: web_server2.py
#Description: Simple web server

#import socket module
from socket import *
import sys # In order to terminate the program

SERVER_PORT = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('', SERVER_PORT))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve on port ' + str(SERVER_PORT))
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:
        message = connectionSocket.recv(2048).decode() #Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start     #Fill in end

        #Send one HTTP header line into socket
        #Fill in start
        httpOK = 'HTTP/1.1 200 OK\r\n'
        connectionSocket.send(httpOK.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (404)
        #Fill in start
        httpNotFound = 'HTTP/1.1 404 NOT FOUND\r\n'
        connectionSocket.send(httpNotFound.encode())

        #Fill in end

        #Close client socket
        #Fill in start
    connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data


