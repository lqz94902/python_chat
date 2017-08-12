# -*- coding: utf-8 -*

import socket
import threading#多线程模块

con=threading.Condition()#线程同步 锁
host=raw_input('input the servers ip address:')
port=1254
data=''     #文本

s=socket.socket()   #创建了一个服务
print ('socket created')
s.bind((host,port))#绑定
s.listen(1)#监听连接

print 'socket new listening'

def NotifyAll(sss):
    global data
    if con.acquire():#获取锁
        data=sss
        con.notifyAll()#表示当前线程放弃时对资源的关闭,通知其他线程从
        con.release()   #释放锁

def threadOut(conn,nick):
    global data
    while 1:
        if con.acquire():   #加锁
            con.wait()      #会堵塞这里 放弃对当前资源占用 等通知
            if data:
                try:
                    conn.send(data)
                    con.release()   #释放锁
                except:
                    con.release()
                    return

def ThreadIn(conn,nick):
    while 1:
        try:
            temp=conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print data
        except:
            NotifyAll(nick+'error')
            print data
            return


while 1:        #为了一直监听
    conn,addr=s.accept()    #接收到连接了
    print 'Connectd with'+addr[0]+':'+str(addr[1])
    nick=conn.recv(1024)
    NotifyAll('Welcome'+':'+'to the room!')
    print data
    conn.send(data)
    threading.Thread(target=threadOut,args=(conn,nick)).start()
