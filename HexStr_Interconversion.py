#Author:蔡学超
#Date:  20190410
#Func: 十六进制串和ASCII字符串互转

from tkinter import *
import binascii
import os
import tkinter.font as tkFont

#转换命令Hex2Str
def Hex2Str():
    src_h_str=h.get()
    mid_h_str1 = bytearray (src_h_str,'GB18030')
    mid_h_str2 = binascii.a2b_hex(mid_h_str1)
    des_h_str  = mid_h_str2.decode('GB18030')
    s.set(des_h_str)

#转换命令Str2Hex
def Str2Hex():
    src_s_str=s.get()
    mid_s_str1 = bytearray (src_s_str,'GB18030')
    mid_s_str2 = binascii.b2a_hex(mid_s_str1)
    des_s_str  = mid_s_str2.decode('GB18030')
    h.set(des_s_str)

#退出cmd
def fquit():
    frame.destroy()
    os._exit(0)
    
root = Tk()
root.iconbitmap('C:/Users/cxc/Desktop/py2exe/Hex2Str.ico')
root.title("十六进制串和ACSII码字符串互转")
frame = Frame(root)
frame.pack(padx=100,pady=50,expand = 1)

lab0 = Label(frame, bg='blue',text="Author:蔡学超",font=tkFont.Font(size=15))
lab0.grid(row=0, column=0,padx=5,pady=40, sticky=N)

lab1 = Label(frame, text="十六进制串:",font=tkFont.Font(size=15))
lab1.grid(row=1, column=0, padx=5, pady=10,sticky=W)

lab2 = Label(frame, text="ASCII字符串:",font=tkFont.Font(size=15))
lab2.grid(row=2, column=0, padx=5, pady=10,sticky=W)


#h是hex,绑定lab1
h = StringVar()
ent1 = Entry(frame, textvariable=h)
ent1.grid(row=1, column=1, sticky='ew', columnspan=3)

#s是str，绑定lab2
s = StringVar()
ent2 = Entry(frame, textvariable=s)
ent2.grid(row=2, column=1, sticky='ew', columnspan=3)

#Button为command
button0 = Button(frame, fg="green",text="Change", command=Hex2Str, default='active',font=tkFont.Font(size=16))
button0.grid(row=1, column=4,columnspan=2,padx=10,pady=20,ipadx=10,ipady=5)

button1 = Button(frame, fg="green",text="Change", command=Str2Hex, default='active',font=tkFont.Font(size=16))
button1.grid(row=2, column=4,columnspan=2,padx=10,pady=20,ipadx=10,ipady=5)

#退出按钮
button2 = Button(frame, fg="red",text="退出", command=fquit, default='disabled',font=tkFont.Font(size=16))
button2.grid(row=3, column=1,columnspan=3,padx=10,pady=20,ipadx=20,ipady=5)


#调整窗口居中显示
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
