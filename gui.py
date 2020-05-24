import sys
#sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import os
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
#import image
from PIL import Image, ImageTk
from functools import partial

# アプリケーション（GUI）クラス
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        img = Image.open("test.jpg")
        self.plName = ["Player1","Player2"]
        self.lp = [8000,8000]

        self.CreateMenubar()
        self.CreateWigets()
        self.DisplayImage(image=img)
        self.DisplayLP()

    #メニューバーを作成
    def CreateMenubar(self): 
        self.menubar = tk.Menu(root)

        #終了
        fileMenu = tk.Menu(self.menubar, tearoff=0)
        #filemenu.add_command(label="Open", command=self.File_open)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        configMenu = tk.Menu(self.menubar, tearoff=0)
        #文字色変更
        configMenu.add_command(label="ChangeColor")
        #configmenu.add_separator()
        #(表示位置変更)
        #configmenu.add_command(label="ChangePlace")
        self.menubar.add_cascade(label="Config", menu=configMenu)

        lpMenu = tk.Menu(self.menubar, tearoff=0)
        #ダメージログ
        lpMenu.add_command(label="Log")
        lpMenu.add_separator()
        #LP初期化
        lpMenu.add_command(label="Reset")
        self.menubar.add_cascade(label="LifePoint", menu=lpMenu)

        root.config(menu=self.menubar)
        root.config()

    #ボタン等を作成
    def CreateWigets(self):
        boxX = 160
        boxY = 740-200

        #画像を表示するキャンバス
        self.canvas = tk.Canvas(root,width=1280,height=720,relief=tk.RIDGE,bd=0)
        self.canvas.place(x=0,y=10)

        #名前入力バー
        self.nameBox = [tk.Entry(width=30,font=("",15)),tk.Entry(width=30,font=("",15))]
        #LP入力バー
        self.lpBox = [tk.Entry(width=30,font=("",15)),tk.Entry(width=30,font=("",15))]
        #+ボタン
        #plusButton = [tk.Button(root,text="+",width=3,font=("",15),command=partial(self.AddLP,0)),tk.Button(root,text="+",width=3,font=("",15),command=partial(self.AddLP,1))]
        #minusButton=[tk.Button(root,text="-",width=3,font=("",15)),tk.Button(root,text="-",width=3,font=("",15))]
        #÷ボタン
        #divButton=[tk.Button(root,text="÷",width=3,font=("",15)),tk.Button(root,text="÷",width=3,font=("",15))]
        #変更ボタン
        #changeButton=[tk.Button(root,text="変更",width=3,font=("",15)),tk.Button(root,text="変更",width=3,font=("",15))]

        for i in range(2):
            self.nameBox[i].place(x=boxX,y=boxY)
            self.nameBox[i].insert(tk.END,'PLAYER'+str(i+1))

            self.lpBox[i].place(x=boxX,y=boxY+30)
            self.lpBox

            plusButton = tk.Button(root,text="+",width=3,font=("",15),command=partial(self.AddLP,i))
            plusButton.place(x=boxX-87,y=boxY-5)
            minusButton = tk.Button(root,text="-",width=3,font=("",15),command=partial(self.SubLP,i))
            minusButton.place(x=boxX-45,y=boxY-5)
            divButton = tk.Button(root,text="÷",width=3,font=("",15),command=partial(self.DivLP,i))
            divButton.place(x=boxX-87,y=boxY+30)
            changeButton = tk.Button(root,text="変更",width=3,font=("",15),command=partial(self.ChangeLP,i))
            changeButton.place(x=boxX-45,y=boxY+30)
            
            boxX = 900
    
    #映像を表示
    def DisplayImage(self,image):
        #self.img_temp = ImageTk.PhotoImage(Image.fromarray(image))
        self.disp = ImageTk.PhotoImage(image)
        self.canvas.create_image(0,0,image=self.disp,anchor=tk.NW)

    #LPを表示
    def DisplayLP(self):
        pl1Text = self.plName[0] + "\nLP:" + str(self.lp[0])
        self.lp1Label = tk.Label(root,text=pl1Text,font=("",30),justify="left")
        self.lp1Label.place(x=20,y=20)
        pl2Text = self.plName[1] + "\nLP:" + str(self.lp[1])
        self.lp2Label = tk.Label(root,text=pl2Text,font=("",30),justify="right")
        self.lp2Label.place(x=1120,y=20)

    #LP加算
    def AddLP(self,num):
        val = self.lpBox[num].get()
        self.lp[num] += int(val)
        self.lpBox[num].delete(0,tk.END)
        self.lp1Label.destroy()
        self.DisplayLP()

    #LP減算
    def SubLP(self,num):
        val = int(self.lpBox[num].get())
        self.lp[num] -= val
        self.lpBox[num].delete(0,tk.END)
        self.lp1Label.destroy()
        self.DisplayLP()

    #LP除算
    def DivLP(self,num):
        self.lp[num] /= 2
        self.lpBox[num].delete(0,tk.END)
        self.lp1Label.destroy()
        self.DisplayLP()

    #LP変更
    def ChangeLP(self,num):
        val = int(self.lpBox[num].get())
        self.lp[num] = val
        self.lpBox[num].delete(0,tk.END)
        self.lp1Label.destroy()
        self.DisplayLP()


# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("CalculatorOverlay") # タイトル
myapp.master.geometry("1280x800") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()