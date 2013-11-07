#!/usr/bin/env python
from socket import *       
#create socket                     
serverSocket = socket(AF_INET, SOCK_STREAM)

#bind server socket to port 8080 and allow it to listen for incoming connections
serverSocket.bind(('', 8889))
serverSocket.listen(1)

print "Server Ready..."
while True:
    try:
	#if client connects on the port, accept the connection
        connectionSocket, addr =  serverSocket.accept()
	#accept the client's incoming message
        message = connectionSocket.recv(32678)
	#print the received message from the client
        print "received data:", message
	#split the message and use string functions to get file name
        filename = message.split()[1]
        filename = filename.replace('/','')
        filename = filename.strip(' ')
	#print the requested file
        print "requested file:", filename
	#open the requested file
        f = open(filename)
        #read the contents of index.html into outputdata
        outputdata = f.read()
        #send one HTTP header line into socket proceeded by data
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
	#send data one byte at a time over the connection
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    #if client requests a file not on server, show 404
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head><title>404</title></head><body><h1>404 File Not Found</h1><br />The file you requested was not found on the server.<hr /></body></html>")
        connectionSocket.close()
    #if an error occurs, print the error
    except Exception as ex:
        print(ex)
        connectionSocket.close()
serverSocket.close()
