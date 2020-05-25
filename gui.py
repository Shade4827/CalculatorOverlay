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
        self.boxPlace = [[160,740-200],[900,740-200]]
        self.lp = [8000,8000]
        self.lpPlace = [[20,20],[1120,20]]
        self.lpLabel = [tk.Label(root),tk.Label(root)]

        self.CreateMenubar()
        self.CreateWigets()
        self.DisplayImage(image=img)
        self.DisplayLP(0)
        self.DisplayLP(1)

    #メニューバーを作成
    def CreateMenubar(self): 
        self.menubar = tk.Menu(root)

        #終了
        fileMenu = tk.Menu(self.menubar, tearoff=0)
        fileMenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        configMenu = tk.Menu(self.menubar, tearoff=0)
        #(表示位置変更)
        #configmenu.add_command(label="ChangePlace")
        self.menubar.add_cascade(label="Config", menu=configMenu)

        lpMenu = tk.Menu(self.menubar, tearoff=0)
        #ダメージログ
        lpMenu.add_command(label="Log")
        lpMenu.add_separator()
        #LP初期化
        lpMenu.add_command(label="Reset",command=self.initLP)
        self.menubar.add_cascade(label="LifePoint", menu=lpMenu)

        root.config(menu=self.menubar)
        root.config()

    #ボタン等を作成
    def CreateWigets(self):
        #画像を表示するキャンバス
        self.canvas = tk.Canvas(root,width=1280,height=720,relief=tk.RIDGE,bd=0)
        self.canvas.place(x=0,y=10)

        #名前入力バー
        self.nameBox = [tk.Entry(width=30,font=("",15)),tk.Entry(width=30,font=("",15))]
        #LP入力バー
        self.lpBox = [tk.Entry(width=30,font=("",15)),tk.Entry(width=30,font=("",15))]

        for i in range(2):
            self.nameBox[i].place(x=self.boxPlace[i][0],y=self.boxPlace[i][1])
            self.nameBox[i].insert(tk.END,'PLAYER'+str(i+1))

            self.lpBox[i].place(x=self.boxPlace[i][0],y=self.boxPlace[i][1]+30)

            plusButton = tk.Button(root,text="+",width=3,font=("",15),command=partial(self.AddLP,i))
            plusButton.place(x=self.boxPlace[i][0]-87,y=self.boxPlace[i][1]-5)
            minusButton = tk.Button(root,text="-",width=3,font=("",15),command=partial(self.SubLP,i))
            minusButton.place(x=self.boxPlace[i][0]-45,y=self.boxPlace[i][1]-5)
            divButton = tk.Button(root,text="÷",width=3,font=("",15),command=partial(self.DivLP,i))
            divButton.place(x=self.boxPlace[i][0]-87,y=self.boxPlace[i][1]+30)
            changeButton = tk.Button(root,text="変更",width=3,font=("",15),command=partial(self.ChangeLP,i))
            changeButton.place(x=self.boxPlace[i][0]-45,y=self.boxPlace[i][1]+30)
    
    #映像を表示
    def DisplayImage(self,image):
        #self.img_temp = ImageTk.PhotoImage(Image.fromarray(image))
        self.disp = ImageTk.PhotoImage(image)
        self.canvas.create_image(0,0,image=self.disp,anchor=tk.NW)

    #LPを表示
    def DisplayLP(self,num):
        just = "left"
        if num == 1:
            just = "right"

        self.lp[num] = round((self.lp[num] * 2 + 1) // 2)

        plText = self.plName[num] + "\nLP:" + str(self.lp[num])
        self.lpLabel[num] = tk.Label(root,text=plText,font=("",30),justify=just)
        self.lpLabel[num].place(x=self.lpPlace[num][0],y=self.lpPlace[num][1])

    #LP加算
    def AddLP(self,num):
        val = self.lpBox[num].get()
        self.lp[num] += int(val)
        self.lpBox[num].delete(0,tk.END)
        self.lpLabel[num].destroy()
        self.DisplayLP(num)

    #LP減算
    def SubLP(self,num):
        val = int(self.lpBox[num].get())
        self.lp[num] -= val
        if self.lp[num] <= 0:
            self.lp[num] = 0
        self.lpBox[num].delete(0,tk.END)
        self.lpLabel[num].destroy()
        self.DisplayLP(num)

    #LP除算
    def DivLP(self,num):
        self.lp[num] /= 2
        self.lpBox[num].delete(0,tk.END)
        self.lpLabel[num].destroy()
        self.DisplayLP(num)

    #LP変更
    def ChangeLP(self,num):
        val = int(self.lpBox[num].get())
        self.lp[num] = val
        self.lpBox[num].delete(0,tk.END)
        self.lpLabel[num].destroy()
        self.DisplayLP(num)

    #ダメージログ
    def DisplayLog(self):


    #LP初期化
    def initLP(self):
        for i in range(2):
            self.lp[i] = 8000
            self.lpLabel[i].destroy()
            self.DisplayLP(i)


# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("CalculatorOverlay") # タイトル
myapp.master.geometry("1280x800") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()