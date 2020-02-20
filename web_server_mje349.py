'''
Author: Montana Esguerra
Email: mje349@nyu.edu
'''


#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start

HOST = 'localhost'
PORT = 8080

serverSocket.bind((HOST, PORT))

#The parameter to listen specifies the maximum number of queued connections
serverSocket.listen(1)

#Fill in end

while True:
    #Establish the connection
    print('Ready to serve on port ' + str(PORT))

    #"Client Socket"
    connectionSocket, addr = serverSocket.accept()

    #TEST See who connected
    print('Connection made: ' + str(addr))
    try:
        message = connectionSocket.recv(1024).decode
        #TEST see what was received
        print('Server received', repr(message))

        #TEST explicitly use HelloWorld.html
        filename = 'HelloWorld.html'
        f = open(filename, 'rb')
        #filename = message.split(' ')
        #f = open(filename[1:])
        outputdata = f.read(1024)

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n')
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        f.close()

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (404)
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n')

        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()

        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data


