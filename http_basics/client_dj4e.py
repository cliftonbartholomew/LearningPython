import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #python uses unicode, internet comms uses utf-8 - encode is utf-8
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end = '')#print uses unicode, decode puts back from utf-8

mysock.close()


##Some webpages requires 50-150 GET and POST cycles
##GET = client, POST = server


#####This is opening up a port to a webserver using telnet

##command
#telnet data.pr4e.org 80      #telnet opens up a socket on port 80 (the web server) on data.pr4e.org

##response
#Trying 192.241.136.170...
#Connected to data.pr4e.org.
#Escape character is '^]'.

##Command
#GET http://data.pr4e.org/page1.htm HTTP/1.0    #send a GET request to the server for a specific page.
# <ENTER>           #this is where you would add additional headers. if no headers, just send <enter>

##reponse
##header
# HTTP/1.1 200 OK
# Date: Sat, 25 Sep 2021 11:39:20 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Mon, 15 May 2017 11:11:47 GMT
# ETag: "80-54f8e1f004857"
# Accept-Ranges: bytes
# Content-Length: 128
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/html
#
##data
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://data.pr4e.org/page2.htm">
# Second Page</a>.
# </p>
# Connection closed by foreign host.