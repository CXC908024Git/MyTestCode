#Author:蔡学超
#Date:  20190410
#Func:  将输入的十六进制串转换为ASCII字符串

from tkinter import *
import binascii

#转换命令
def submit():
    #p.set(u.get())
    src_str=u.get()
    mid_str1 = bytearray (src_str,'GB18030')
    mid_str2 = binascii.a2b_hex(mid_str1)
    des_str  = mid_str2.decode('GB18030')
    p.set(des_str)
    
root = Tk()
root.iconbitmap('C:/Users/cxc/Desktop/py2exe/Hex2Str.ico')
root.title("十六进制串和ACSII码字符串互转")
frame = Frame(root)
frame.pack(padx=100, pady=80, ipadx=5)

lab0 = Label(frame, text="Author:蔡学超")
lab0.grid(row=0, column=0, padx=5, pady=30,sticky=W)

lab1 = Label(frame, text="源十六进制串:")
lab1.grid(row=1, column=0, padx=5, pady=5, sticky=W)

lab2 = Label(frame, text="ASCII字符串:")
lab2.grid(row=2, column=0, padx=5, pady=5, sticky=W)


#u是输入,绑定lab1
u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=1, column=1, sticky='ew', columnspan=3)

#p是输出，绑定lab2
p = StringVar()
ent2 = Entry(frame, textvariable=p)
ent2.grid(row=2, column=1, sticky='ew', columnspan=3)

#Button为command
button = Button(frame, text="开始转换", command=submit, default='active')
button.grid(row=3, column=1)


#调整窗口居中显示
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
