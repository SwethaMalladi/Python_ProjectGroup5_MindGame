import tkinter as tk
import os
import PIL
from PIL import ImageTk, Image

from HighScore import HighScore
from Instructions import Instructions
from GamePage import GamePlay

class LevelPage:

    def __init__(self):

        self.selected=""

        #Create main Window
        self.level_window = tk.Toplevel()
        self.level_window.configure(bg="white")
        self.level_window.title("Levels")

        self.BASE_DIR = os.path.dirname(__file__)
        small_font = ("Comic Sans MS", 20)

        width = self.level_window.winfo_screenwidth()
        height = self.level_window.winfo_screenheight()
        self.level_window.geometry("%dx%d" % (width, height))

        self.one_frame = tk.Frame(self.level_window, bg="white")
        self.one_frame.config(width=300, height=300)
        self.one_frame.pack(side=tk.LEFT, padx=15, pady=15)
        self.two_frame = tk.Frame(self.level_window, bg="white")
        self.one_frame.config(width=300, height=300)
        self.two_frame.pack(side=tk.LEFT, padx=15, pady=15)
        self.toolFrame = tk.Frame(self.level_window,bg="white")
        self.toolFrame.config(width=300, height=300)
        self.toolFrame.pack(side=tk.TOP,anchor="e", padx=15, pady=15)

        # Create the two frames
        self.fruit_frame = tk.Frame(self.one_frame)
        self.fruit_frame.pack(side=tk.TOP)
        self.fruit_frame.config(width=300, height=300)
        # Creating a photoimage object to use image
        fruits_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\fruitLevelIcon.jpg","rb")
        fruits_photo = PIL.Image.open(fruits_fp)
        fruits_image = ImageTk.PhotoImage(fruits_photo)

        self.fruits_btn = tk.Button(self.fruit_frame, justify='right',image=fruits_image,
                                     relief='flat', bg="white",command=self.playFruitsGame)
        self.fruits_btn.pack(side=tk.TOP, padx=15, pady=15)
        self.fruits_label = tk.Label(self.fruit_frame, text="Fruits", font=40, bg="white")
        self.fruits_label.config(font=small_font)
        self.fruits_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        veg_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\vegetablesLevelIcon.jpg", "rb")
        veg_photo = PIL.Image.open(veg_fp)
        veg_image = ImageTk.PhotoImage(veg_photo)

        self.veg_frame = tk.Frame(self.one_frame)
        self.veg_frame.config(width=300, height=300)
        self.veg_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.veg_img = tk.Button(self.veg_frame, justify='right', image=veg_image,
                                   relief='flat', bg="white",command=self.playVegetableGame)
        self.veg_img.pack(side=tk.TOP, padx=15, pady=15)
        self.veg_label = tk.Label(self.veg_frame, text="Vegetables", font=40, bg="white")
        self.veg_label.config(font=small_font)
        self.veg_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        num_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\NumbersLevelIcon.jpg", "rb")
        num_photo = PIL.Image.open(num_fp)
        num_image = ImageTk.PhotoImage(num_photo)

        self.num_frame = tk.Frame(self.two_frame)
        self.num_frame.config(width=300, height=300)
        self.num_frame.pack(side=tk.TOP)
        self.num_img = tk.Button(self.num_frame, justify='right', image=num_image,
                                        relief='flat', bg="white",command=self.playNumbersGame)
        self.num_img.pack(side=tk.TOP, padx=15, pady=15)
        self.num_label = tk.Label(self.num_frame, text="Numbers", font=40, bg="white")
        self.num_label.config(font=small_font)
        self.num_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        alpha_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\AnimalsLevelIcon.jpg", "rb")
        alpha_photo = PIL.Image.open(alpha_fp)
        alpha_image = ImageTk.PhotoImage(alpha_photo)

        self.alpha_frame = tk.Frame(self.two_frame)
        self.alpha_frame.config(width=300, height=300)
        self.alpha_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.alpha_img = tk.Button(self.alpha_frame, justify='right', image=alpha_image,
                                         relief='flat', bg="white",command=self.playAlphabetGame)
        self.alpha_img.pack(side=tk.TOP, padx=15, pady=15)
        self.alpha_label = tk.Label(self.alpha_frame, text="Animals", font=40, bg="white")
        self.alpha_label.config(font=small_font)
        self.alpha_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        high_score_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\score32.png", "rb")
        high_score_photo = PIL.Image.open(high_score_fp)
        highScore_image = ImageTk.PhotoImage(high_score_photo)

        self.high_score = tk.Button(self.toolFrame, justify='right', image=highScore_image,
                                         relief='flat', bg="white",command=self.getHighScore)
        self.high_score.pack(side=tk.LEFT,padx=5,pady=5)

        rules_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\help32.png", "rb")
        rules_photo = PIL.Image.open(rules_fp)
        rules_image = ImageTk.PhotoImage(rules_photo)

        self.rules = tk.Button(self.toolFrame, justify='right', image=rules_image,
                                    relief='flat', bg="white",command=self.getInstructions)
        self.rules.pack(side=tk.LEFT, padx=5, pady=5)

        back_fp = open(rb"C:\Users\sweth\OneDrive\Desktop\swetha\Python\Mind_Game\res\Images\cancel32.png", "rb")
        back_photo = PIL.Image.open(back_fp)
        back_image = ImageTk.PhotoImage(back_photo)

        self.back = tk.Button(self.toolFrame, justify='right', image=back_image,
                               relief='flat', bg="white",command=self.goBack)
        self.back.pack(side=tk.LEFT, padx=5, pady=5)

        self.level_window.mainloop()

    def getHighScore(self):
        highScore = HighScore()
    def getInstructions(self):
        instructions = Instructions()
    def goBack(self):
        self.level_window.destroy()
    def playFruitsGame(self):
        gamePlay = GamePlay("Fruits")
        gamePlay.play()
    def playVegetableGame(self):
        gamePlay = GamePlay("Vegetables")
        gamePlay.play()
    def playNumbersGame(self):
        gamePlay = GamePlay("Numbers")
        gamePlay.play()
    def playAlphabetGame(self):
        gamePlay = GamePlay("Animals")
        gamePlay.play()



