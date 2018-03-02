import socket
import time
import urllib.request, urllib.error, urllib.parse
import re
from bs4 import BeautifulSoup
import ssl

#fetch document
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()

#retrieve image

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b"" #bytes literal

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    time.sleep(0.25)
    count += len(data)
    print(len(data), count)
    picture += data
#
# mysock.close()

# look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

#skip past header and save the picture data

picture = picture[pos + 4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

#using urlib
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#parsing HTML and scraping web

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())

#parsing HTML using BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

#reading binary files using urllib

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover.jpg', 'wb')
# fhand.write(img)
# fhand.close()
size = 0
#retrieve data in blocks

while True:
    info = img.read(100000) #AttributeError: 'bytes' object has no attribute 'read'
    if len(info) < 0:
        break
    size += len(info)
    fhand = write(info)

print(size, 'characters copied.')
fhand.close()