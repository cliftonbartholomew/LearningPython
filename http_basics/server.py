from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()  # accept is a blocking method.

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")

            if len(pieces) > 0:
                print(pieces[0])

            #how the data response is built up is based on the http protocol. 200 is OK, 404 is not found
            # header
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset = utf-8\r\n"
            data += "\r\n"
            # data
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")

    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print("Access http://localhost:9000")
createServer()
