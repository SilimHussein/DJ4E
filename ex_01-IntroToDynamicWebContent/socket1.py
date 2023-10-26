#simple browser. we start by importing a socket
import socket

#then we create a socket. think of it like a phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#then make a connection, think of it as making a phone call, has a domain and port number.
mysock.connect(('data.pr4e.org', 80))

#then we send a command, get, space, url, space, hhtp and two blank lines, then we encode utf8.
cmd = 'GET http://data.pr4e.org/page1/htm HTTP/1.0\r\n\r\n'.encode()

#send the request. eg. scripting telnet. 
mysock.send(cmd)

#loop to receive data until the socket close.
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()