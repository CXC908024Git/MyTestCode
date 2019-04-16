import PythonMagick
import tkinter
import os
from tkinter import Tk
from tkinter import filedialog
from tkinter import *
from tkinter import font as tkFont


root = Tk()

def tksize(w,h):
    req_w = root.winfo_reqwidth()
    req_h = root.winfo_reqheight()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2 - (w-req_w)/2
    y = (root.winfo_screenheight() - root.winfo_reqheight())/2 - (h-req_h)/2
    root.geometry('%dx%d+%d+%d' % (w,h,x,y))

#浏览命令Scan
def Scan():
    global src_path
    file_path = filedialog.askopenfilename()
    src.set(file_path)
    src_path = src.get()
    

#保存命令Scan
def Save():
    global des_path
    file_path = filedialog.asksaveasfilename(filetypes=[('image', '*.*')])
    des.set(file_path)
    des_path = des.get()

#转换命令Scan
def Change():
    w_size=int(wid.get())
    h_size=int(hei.get())
    
    img = PythonMagick.Image(src_path)
    #尺寸可调
    img.sample('%dx%d' % (h_size,w_size))
    img.write(des_path)

#退出cmd
def fquit():
    frame.destroy()
    os._exit(0)

tksize(600,350)
root.title('PicFromatChg')
root.iconbitmap('C:/Users/cxc/Desktop/py2exe/she.ico')

frame = Frame(root)
frame.pack(padx=100,pady=50,expand = 1)

#固定几个标签
lab0 = Label(frame, bg='blue',text="Author:蔡学超",font=tkFont.Font(size=13))
lab0.grid(row=0, column=0, sticky=W)

lab1 = Label(frame, text="源图片:",font=tkFont.Font(size=12))
lab1.grid(row=1, column=0, sticky=W)

lab2 = Label(frame, text="目标:",font=tkFont.Font(size=12))
lab2.grid(row=2, column=0, pady=10,sticky=W)

lab3 = Label(frame, text="长(像素):",font=tkFont.Font(size=10))
lab3.grid(row=3, column=0,sticky=W)

lab4 = Label(frame, text="高(像素):",font=tkFont.Font(size=10))
lab4.grid(row=4, column=0,sticky=W)

#src是源目标文件路径,绑定lab1
src = StringVar()
ent1 = Entry(frame, textvariable=src)
ent1.grid(row=1, column=1, columnspan=1, sticky=W)

#des是目标文件路径，绑定lab2
des = StringVar()
ent2 = Entry(frame, textvariable=des)
ent2.grid(row=2, column=1, columnspan=1, sticky=W)

#wid是目标图片像素
wid = StringVar()
ent3 = Entry(frame, textvariable=wid)
ent3.grid(row=3, column=1, pady=5)

#hei是目标图片像素
hei = StringVar()
ent4 = Entry(frame, textvariable=hei)
ent4.grid(row=4, column=1, pady=2)

button0 = Button(frame, fg="green",text="浏览", command=Scan, default='active',font=tkFont.Font(size=13))
button0.grid(row=1, column=3,columnspan=2)

button1 = Button(frame, fg="green",text="保存", command=Save, default='active',font=tkFont.Font(size=13))
button1.grid(row=2, column=3,columnspan=2)

button2 = Button(frame, fg="blue",text="转换", command=Change, default='active',font=tkFont.Font(size=13))
button2.grid(row=6, column=0,columnspan=2,ipadx=10,pady=20,ipady=5, sticky=W)

button2 = Button(frame, fg="red",text="退出", command=fquit, default='disabled',font=tkFont.Font(size=13))
button2.grid(row=6, column=2,columnspan=2,ipadx=10,pady=20,ipady=5, sticky=E)

root.mainloop()
