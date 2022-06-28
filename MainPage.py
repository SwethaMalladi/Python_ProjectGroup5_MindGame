import tkinter as tk
import os
import PIL
from PIL import ImageTk, Image

from LevelPage import LevelPage


class MainPage:

    def __init__(self):
        self.BASE_DIR = os.path.dirname(__file__)
        Font_tuple = ("Comic Sans MS", 80)

        #Create main Window
        self.main_window = tk.Tk()
        self.main_window.configure(bg="white")
        width = self.main_window.winfo_screenwidth()
        height = self.main_window.winfo_screenheight()
        self.main_window.geometry("%dx%d" % (width, height))
        self.main_window.title("Mind Game")


        self.main_window.config(background="white")

        self.one_frame = tk.Frame(self.main_window,bg="white")
        self.one_frame.pack(anchor="w", padx=15, pady=15)

        title_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\brain.jpg", "rb")
        title_photo = PIL.Image.open(title_fp)
        title_img = ImageTk.PhotoImage(title_photo)

        self.title_label = tk.Label(self.one_frame,image=title_img,bg="white")
        self.title_label.pack(anchor="c",side=tk.LEFT)


        start_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\start.jpg", "rb")
        start_photo = PIL.Image.open(start_fp)
        start_image = ImageTk.PhotoImage(start_photo)

        self.play_image = tk.Label(self.one_frame, image=start_image,bg="white")
        self.play_image.pack(anchor="e",side=tk.LEFT)

        self.play_label = tk.Button(self.one_frame,text="start",relief='flat',fg="green", bg="white",command=self.levelPage)
        self.play_label.configure(font=Font_tuple)
        self.play_label.pack(anchor="e", side=tk.RIGHT)

        boyA_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\boyAlphabet.jpg", "rb")
        boyA_photo = PIL.Image.open(boyA_fp)
        boy_A = ImageTk.PhotoImage(boyA_photo)

        self.boy_A_image = tk.Label(self.main_window, image=boy_A, bg="white")
        self.boy_A_image.pack(side=tk.LEFT)

        girlN_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\girlNumber.jpg", "rb")
        girlN_photo = PIL.Image.open(girlN_fp)
        girl_N = ImageTk.PhotoImage(girlN_photo)

        self.girl_N_image = tk.Label(self.main_window, image=girl_N, bg="white")
        self.girl_N_image.pack(side=tk.LEFT)

        boyV_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\boyVegetable.jpg", "rb")
        boyV_photo = PIL.Image.open(boyV_fp)
        boy_V = ImageTk.PhotoImage(boyV_photo)

        self.boy_V_image = tk.Label(self.main_window, image=boy_V, bg="white")
        self.boy_V_image.pack(side=tk.LEFT)

        boyF_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\boyFruit.jpg", "rb")
        boyF_photo = PIL.Image.open(boyF_fp)
        boy_F = ImageTk.PhotoImage(boyF_photo)

        self.boy_F_image = tk.Label(self.main_window, image=boy_F, bg="white")
        self.boy_F_image.pack(side=tk.LEFT)

        girlH_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\girlHalloween.png", "rb")
        girlH_photo = PIL.Image.open(girlH_fp)
        girl_H = ImageTk.PhotoImage(girlH_photo)

        self.boy_F_image = tk.Label(self.main_window, image=girl_H, bg="white")
        self.boy_F_image.pack(side=tk.LEFT)


        self.main_window.mainloop()

    def levelPage(self):
        print("Start Level Page")
        level = LevelPage()

    def exitGame(self):
        self.main_window.destroy()
mainPage =MainPage()
