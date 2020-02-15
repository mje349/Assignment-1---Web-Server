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

#I arbitrarily choose port 8080 for testing
serverPort = 8080
serverSocket.bind(('localhost', serverPort))

#The parameter to listen specifies the maximum number of queued connections
serverSocket.listen(1)

#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')

    #"Client Socket"
    connectionSocket, addr = '''Fill in start ''' serverSocket.accept() ''''Fill in end'''
    try:
        message = '''Fill in start''' connectionSocket.recv(1024).decode '''Fill in end'''
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = '''Fill in start ''' "HelloWorld.html"  '''#Fill in end'''

        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n')
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (404)
        #Fill in start

        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()

        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data


