import urllib.request

#this is an abstracted url object that handles opening a socket on a port
#closes the port and saves all the url data into fhand
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

for line in fhand:
    print(line.decode().strip())