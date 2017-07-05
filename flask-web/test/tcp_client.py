#!/usr/bin/env python
#encoding:utf8

from socket import *

#HOST = 'localhost'
#PORT = 21567
#HOST = '192.168.1.100'
HOST = '192.168.30.26'
PORT = 8081
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 客户端和服务端都需要关闭连接。
while True:
    data = raw_input('> ')
    if not data:
        break
    with open('req.txt', 'rb') as fo:
        data=fo.read()
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    print 'a:', data
    data = tcpCliSock.recv(BUFSIZ)
    print 'b:', data
    if not data:
        break
    #print data

tcpCliSock.close()
