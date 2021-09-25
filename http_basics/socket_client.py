import socket

#sockets are a fundamental concept in networking. HTTP communication is HOW
#to communicate over those sockets.

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode() #python uses unicode, internet comms uses utf-8 - encode is utf-8
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end = '')#print uses unicode, decode puts back from utf-8

mysock.close()
