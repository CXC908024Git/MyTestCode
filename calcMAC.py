#coding=utf-8
#Auoth:蔡学超
import socket
from tkinter import *
import binascii
import os
import tkinter.font as tkFont

#HostIP = '192.168.100.6'
#HostPort = 51110
#验MACreqMS = "55251101600200 196200389990000002173 460000 000000003000 0812095500 008500 7011 00 0848100000 0848100000 12345678 123456789012345 196200389990000002173 16620515703000001076094DE54808"
#算MACreqMS = "55250101600200 196200389990000002173 460000 000000003000 0812095500 008500 7011 00 0848100000 0848100000 12345678 123456789012345 196200389990000002173 1662051570300000104808"

root = Tk()
root.title("MAC工具")
frame = Frame(root)
frame.pack(padx=100,pady=50,expand = 1)

#ask4ans
def ask4ans():
    des_ip  = ads.get()
    des_pot = pot.get()
    req_msg = req.get()
    tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (des_ip, int(des_pot))
    tcpCliSock.connect(address)

    req_send = chr(0).encode() + bytes(bytearray((len(req_msg),))) + req_msg.encode()
    tcpCliSock.send(req_send)
    res_msg = tcpCliSock.recv(1024).decode()
    des_res = res_msg[8:]

    tcpCliSock.close
    
    rsp.set(des_res)

#退出cmd
def fquit():
    frame.destroy()
    os._exit(0)

lab0 = Label(frame, text="加密机IP:",font=tkFont.Font(size=15))
lab0.grid(row=0, column=0,padx=5,pady=8, sticky=W)

lab1 = Label(frame, text="端口:",font=tkFont.Font(size=15))
lab1.grid(row=1, column=0, padx=5, pady=8,sticky=W)

lab2 = Label(frame, text="请求字符串:",font=tkFont.Font(size=15))
lab2.grid(row=2, column=0, padx=5, pady=8,sticky=W)

lab3 = Label(frame, text="应答字符串:",font=tkFont.Font(size=15))
lab3.grid(row=3, column=0, padx=5, pady=8,sticky=W)

ads = StringVar()
ent0 = Entry(frame, textvariable=ads)
ent0.grid(row=0, column=1, sticky='ew', columnspan=3)

pot = StringVar()
ent1 = Entry(frame, textvariable=pot)
ent1.grid(row=1, column=1, sticky='ew', columnspan=3)

req = StringVar()
ent2 = Entry(frame, textvariable=req)
ent2.grid(row=2, column=1, sticky='ew', columnspan=3)

rsp = StringVar()
ent3 = Entry(frame, textvariable=rsp)
ent3.grid(row=3, column=1, sticky='ew', columnspan=3)

button0 = Button(frame, fg="green",text="Send", command=ask4ans, default='active',font=tkFont.Font(size=16))
button0.grid(row=4, column=0,columnspan=2,padx=10,pady=10,ipadx=5,ipady=3,sticky=W)

button1 = Button(frame, fg="red",text="Exit", command=fquit, default='disabled',font=tkFont.Font(size=16))
button1.grid(row=4, column=2,columnspan=2,padx=10,pady=10,ipadx=5,ipady=3,sticky=SE)


#调整窗口居中显示
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()

