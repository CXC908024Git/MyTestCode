#Author:蔡学超
#Date  :2019.04.12
#Func  :自定义截图工具

import tkinter
from tkinter import filedialog
from PIL import ImageGrab
from PIL import ImageTk
from PIL import Image
from time import sleep

root = tkinter.Tk()
#root.geometry('100x40+400+300')
#root.geometry('{}x{}+{}+{}'.format(300,100, 0, 0))
root.iconbitmap(bitmap='C:/Users/cxc/Desktop/py2exe/spot.ico')
root. title('Spot by xccai')

#居中显示TK框
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 100
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 + 30
root.geometry("250x60+%d+%d" % (x, y))

#TK框固定位置
root.resizable(False, False)

class MyCapture:

    def __init__(self, png):

        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        
        #隐藏TK窗口
        self.top.overrideredirect(True)
        
        self.image = Image.open('temp.png')
        self.image = ImageTk.PhotoImage(self.image)

        
        self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
        self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)

        #鼠标左键点击获取起始点坐标
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)
        
        #鼠标移动出现矩形待选择区域
        def onLeftButtonMove(event):
            if not self.sel:
                return

            global lastDraw

            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

        self.canvas.bind('<B1-Motion>', onLeftButtonMove)

        #鼠标左键抬起弹出TK对话框并截图保存
        def onLeftButtonUp(event):

            self.sel = False

            try:

                self.canvas.delete(lastDraw)

            except Exception as e:

                pass

            sleep(0.2)

            left, right = sorted([self.X.get(), event.x])
            top, bottom = sorted([self.Y.get(), event.y])
            
            pic = ImageGrab.grab((left+1, top+1, right, bottom))

            fileName = filedialog.asksaveasfilename(title='保存截图', filetypes=[('image', '*.jpg *.png')])
            if fileName:
                pic.save(fileName+'.jpg')
                self.top.destroy()
            else:
                self.top.destroy()
        
        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

def buttonCaptureClick():

    #最小化主窗口
    root.state('icon')
    sleep(0.2)

    filename = 'temp.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()

    #显示全屏幕截图

    w = MyCapture(filename)
    buttonCapture.wait_window(w.top)

    root.state('normal')
    #os.remove(filename)

#截图按键的位置和指令

buttonCapture = tkinter.Button(root, text='截图', command=buttonCaptureClick)
buttonCapture.place(x=80, y=17, width=80, height=30)


#消息主循环
root.mainloop()

        









        
