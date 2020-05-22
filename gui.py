import sys
#sys.path.append('D:/anaconda3/envs/opencv430/Lib/site-packages')
import os
import numpy as np
import tkinter as tk

import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog

# アプリケーション（GUI）クラス
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.CreateMenubar()
        self.CreateWigets()

    #メニューバーを作成
    def CreateMenubar(self): 
        self.menubar = tk.Menu(root)

        filemenu = tk.Menu(self.menubar, tearoff=0)
        #filemenu.add_command(label="Open", command=self.File_open)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(self.menubar, tearoff=0)
        #editmenu.add_command(label="Grayscale", command=self.Proc_grayscale)
        #editmenu.add_command(label="Binarize", command=self.Proc_binarize)
        self.menubar.add_cascade(label="Processing", menu=editmenu)

        root.config(menu=self.menubar)
        root.config()

    #ボタンを作成
    def CreateWigets(self):
        pw_main = tk.PanedWindow(self.master, orient='horizontal')
        pw_main.pack(expand=True, fill = tk.BOTH, side="left")

        pw_left = tk.PanedWindow(pw_main, bg="cyan", orient='vertical')
        pw_main.add(pw_left)
        pw_right = tk.PanedWindow(pw_main, bg="yellow", orient='vertical')
        pw_main.add(pw_right)

        fm_select = tk.Frame(pw_left, bd=2, relief="ridge")
        pw_left.add(fm_select)

        ## padx , pady ：外側の横、縦の隙間
        label_fpath = tk.Label(fm_select, text="ファイルパス(入力)", width=20)
        ## ラベルを配置
        label_fpath.grid(row=0, column=0, padx=2, pady=2)

        entry_fpath = tk.Entry(fm_select, justify="left", width=50)
        entry_fpath.grid(row=0, column=1, sticky=tk.W + tk.E,padx=2, pady=2)



# 実行
root = tk.Tk()        
myapp = Application(master=root)
myapp.master.title("My Application") # タイトル
myapp.master.geometry("1000x500") # ウィンドウの幅と高さピクセル単位で指定（width x height）

myapp.mainloop()