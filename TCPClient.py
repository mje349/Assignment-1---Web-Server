#Author: Montana Esguerra
#Date: 2/20/20
#Filename: TCPClient.py
#Description: Sample TCP Client program from the textbook

from socket import *

from pip._vendor.distlib.compat import raw_input

SERVER_NAME = 'servername'
SERVER_PORT = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

sentence = raw_input('Input lowercase sentence:')
client_socket.send(sentence.encode())

modified_sentence = client_socket.recv(2048)
print('From Server: ', modified_sentence.decode())

client_socket.close()