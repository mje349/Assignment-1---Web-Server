#Author: Montana Esguerra
#Date: 2/20/20
#Filename: web_server_mje349.py
#Description:
#This is a simple web server that allows for only 1 client to connect at a time.
#This server runs off of localhost on port 12001
#Currently, the server only serves two html pages: HelloWorld.html and notFound.html
#The notFound.html page is served anytime a page not in the directory is requested - this includes index.html
#This is a TCP Web Server - it works with Firefox, Chrome, and Edge without issue.
#To get the notFound.html to display on Internet Explorer, go into settings - Internet Options - Advanced tab -
#Scroll down and uncheck Show friendly HTTP Error Messages

#import socket module
from socket import *
import sys # In order to terminate the program

SERVER_PORT = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('', SERVER_PORT))
serverSocket.listen(1) #So far only allows for 1 connection at a time
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
        f.close()

        #Send one HTTP header line into socket
        #Fill in start
        httpOK = 'HTTP/1.1 200 OK\r\n'
        connectionSocket.send(httpOK.encode())
        connectionSocket.send('Content-Type: text/html\n'.encode())
        connectionSocket.send('\n'.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found (404)
        #Fill in start

        #Prepare to send the 404 Not Found html page
        not_found = open('notFound.html')
        outputNotFound = not_found.read()
        not_found.close()


        httpNotFound = 'HTTP/1.1 404 NOT FOUND\r\n'
        connectionSocket.send(httpNotFound.encode())
        connectionSocket.send('Content-Type: text/html\n'.encode())
        connectionSocket.send('\n'.encode())

        for i in range(0, len(outputNotFound)):
            connectionSocket.send(outputNotFound[i].encode())

        connectionSocket.send("\r\n".encode())
        #Fill in end

        #Close client socket
        #Fill in start
    connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data


