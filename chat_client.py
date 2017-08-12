# -*- coding: utf-8 -*

import socket
import threading#多线程模块

#全局变量
outString=''
nick=''
inString=''


def client_send(sock):
    global outString
    while 1: #死循环，监听输入发送到服务端
        outString=raw_input()#接收输入
        outString=nick+':'+outString#拼接
        sock.send(outString)

def client_accept(sock):
    global inString     #在生产环境，不推荐使用
    while 1:
        try:
            inString=sock.recv(1024)    #接收数据(一次最多1024字节)
            if not inString:#异常处理
                break
            if outString !=inString:
                print inString
        except:
            break


nick=raw_input('input your nickname:')
ip=raw_input('input the server ip address')
port=1254#端口
sock=socket.socket()#创建套接字
sock.connect((ip,port))#连接

sock.send(nick)#将用户名发送到服务端
#发送、接收多线程
th_send=threading.Thread(target=client_send,args=(sock,))#(sock,)来表示元组
th_send.start()#启动
th_accept=threading.Thread(target=client_accept,args=())
th_accept.start()
