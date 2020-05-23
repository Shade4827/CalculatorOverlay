import sys
#sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import os
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
#import image
from PIL import Image, ImageTk

# アプリケーション（GUI）クラス
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.CreateMenubar()
        self.CreateWigets(1)
        self.CreateWigets(2)

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

        lpMenu = tk.Menu(selｆ.menubar, tearoff=0)
        #ダメージログ
        lpMenu.add_command(label="Log")
        lpMenu.add_separator()
        #LP初期化
        lpMenu.add_command(label="Reset")
        self.menubar.add_cascade(label="LifePoint", menu=lpMenu)

        root.config(menu=self.menubar)
        root.config()

    #ボタン等を作成
    def CreateWigets(self,num):
        boxX = 160
        if(num==2):
            boxX = 900
        boxY = 660

        #名前入力バー
        nameBox = tk.Entry(width=30,font=("",15))
        nameBox.place(x=boxX,y=boxY)
        nameBox.insert(tk.END,'PLAYER'+str(num))
        #LP入力バー
        lpBox = tk.Entry(width=30,font=("",15))
        lpBox.place(x=boxX,y=boxY+30)

        #btn=tk.Button(root,text="test",width=5)
        #btn.place(x=20,y=20)
        #+ボタン
        plusButton=tk.Button(root,text="+",width=3,font=("",15))
        plusButton.place(x=boxX-87,y=boxY-5)
        #-ボタン
        minusButton=tk.Button(root,text="-",width=3,font=("",15))
        minusButton.place(x=boxX-45,y=boxY-5)
        #÷ボタン
        divButton=tk.Button(root,text="÷",width=3,font=("",15))
        divButton.place(x=boxX-87,y=boxY+30)
        #変更ボタン
        changeButton=tk.Button(root,text="変更",width=3,font=("",15))
        changeButton.place(x=boxX-45,y=boxY+30)
        

# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("CalculatorOverlay") # タイトル
myapp.master.geometry("1280x720") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()