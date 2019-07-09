#Author:蔡学超
#Date:  20190410
#Func: 十进制/十六进制串和ASCII字符串互转

from tkinter import *
import binascii
import os
import tkinter.font as tkFont


#10进制和16进制相互转换函数定义
def dec2hex(str1):
    a = str(hex(eval(str1)))
    b = a.replace("0x",'')
    return b

def hex2dec(str1):
    b = eval("0x" + str1)
    a = str(b).replace("0x",'')
    return b

#转换命令Dec2oth
def Dec2oth():
    src_d_str = d.get()
    src_d2h=dec2hex(src_d_str)
    mid_h_str1 = bytearray (src_d2h,'GB18030')
    mid_h_str2 = binascii.a2b_hex(mid_h_str1)
    des_h_str  = mid_h_str2.decode('GB18030')
    s.set(des_h_str)
    h.set(src_d2h)


#转换命令Hex2oth
def Hex2oth():
    src_h_str = h.get()
    src_h2d=hex2dec(src_h_str)
    mid_h_str1 = bytearray (src_h_str,'GB18030')
    mid_h_str2 = binascii.a2b_hex(mid_h_str1)
    des_h_str  = mid_h_str2.decode('GB18030')
    s.set(des_h_str)
    d.set(src_h2d)

#转换命令Str2oth
def Str2oth():
    src_s_str = s.get()
    mid_s_str1 = bytearray (src_s_str,'GB18030')
    mid_s_str2 = binascii.b2a_hex(mid_s_str1)
    des_s_str  = mid_s_str2.decode('GB18030')
    src_s2d = hex2dec(des_s_str)
    h.set(des_s_str)
    d.set(src_s2d)

#退出cmd
def fquit():
    frame.destroy()
    os._exit(0)
    
root = Tk()
root.iconbitmap('C:/Users/cxc/Desktop/py2exe/DHS_CHG.ico')
root.title("十进制/十六进制串和ASCII字符串互转")
frame = Frame(root)
frame.pack(padx=100,pady=50,expand = 1)

lab0 = Label(frame, bg='blue',text="Author:蔡学超",font=tkFont.Font(size=15))
lab0.grid(row=0, column=0,padx=5,pady=40, sticky=N)

lab1 = Label(frame, text="十进制串:",font=tkFont.Font(size=15))
lab1.grid(row=1, column=0, padx=5, pady=10,sticky=W)

lab2 = Label(frame, text="十六进制串:",font=tkFont.Font(size=15))
lab2.grid(row=2, column=0, padx=5, pady=10,sticky=W)

lab3 = Label(frame, text="ASCII字符串:",font=tkFont.Font(size=15))
lab3.grid(row=3, column=0, padx=5, pady=10,sticky=W)


#d是dec,绑定lab1
d = StringVar()
ent1 = Entry(frame, textvariable=d)
ent1.grid(row=1, column=1, sticky='ew', columnspan=3)

#h是hex,绑定lab2
h = StringVar()
ent2 = Entry(frame, textvariable=h)
ent2.grid(row=2, column=1, sticky='ew', columnspan=3)

#s是str，绑定lab3
s = StringVar()
ent3 = Entry(frame, textvariable=s)
ent3.grid(row=3, column=1, sticky='ew', columnspan=3)

#Button为command
button0 = Button(frame, fg="green",text="Change", command=Dec2oth, default='active',font=tkFont.Font(size=16))
button0.grid(row=1, column=4,columnspan=2,padx=10,pady=20,ipadx=10,ipady=3)

button0 = Button(frame, fg="green",text="Change", command=Hex2oth, default='active',font=tkFont.Font(size=16))
button0.grid(row=2, column=4,columnspan=2,padx=10,pady=20,ipadx=10,ipady=3)

button1 = Button(frame, fg="green",text="Change", command=Str2oth, default='active',font=tkFont.Font(size=16))
button1.grid(row=3, column=4,columnspan=2,padx=10,pady=20,ipadx=10,ipady=3)

#退出按钮
button2 = Button(frame, fg="red",text="退出", command=fquit, default='disabled',font=tkFont.Font(size=16))
button2.grid(row=4, column=1,columnspan=3,padx=10,pady=20,ipadx=20,ipady=5)


#调整窗口居中显示
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
