from tkinter import Tk
#from tkinter import Frame
from tkinter import *
from tkinter import font
root = Tk()

#长宽可调的居中的Tk框
req_w = root.winfo_reqwidth()
req_h = root.winfo_reqheight()
w = 600
h = 400
k1 = w/req_w
x = (root.winfo_screenwidth() - root.winfo_reqwidth())/2 - (w-req_w)/2
y = (root.winfo_screenheight() - root.winfo_reqheight())/2 - (h-req_h)/2
root.geometry('%dx%d+%d+%d' % (w,h,x,y))
root.title('Mycode')

fon1 = font.Font(size=16)

f1=Frame(root,bg='green',width=400,height=100)
f2=Frame(root,bg='red',width=200,height=100)

f1.pack(side=LEFT,anchor=N,fill=Y)
f2.pack(side=LEFT)



