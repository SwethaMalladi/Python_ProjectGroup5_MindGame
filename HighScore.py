import tkinter as tk
import os
import PIL
from PIL import ImageTk, Image


class HighScore:

    def __init__(self,*args):

        self.BASE_DIR = os.path.dirname(__file__)
        self.RESOURCE_PATH = os.path.join(self.BASE_DIR, 'res')
        self.IMAGE_PATH = os.path.join(self.RESOURCE_PATH, 'Images')

        self.currentScore = 0
        self.highScore = self.file_open_read()
        if len(args) == 0:
            self.currentScore = "Let's break the Highest Score\n"
        else:
            if args[0] > int(self.highScore):
                self.currentScore = "New Best Score is " + str(args[0])
                self.file_open_write(str(args[0]))
            else:
                self.currentScore = "Collected "+str(args[1])+" Your Score is " + str(args[0])

        self.BASE_DIR = os.path.dirname(__file__)
        Font_tuple = ("Comic Sans MS", 60)
        smallFont_tuple = ("Comic Sans MS", 40)

        #Create main Window
        self.highScore_frame = tk.Toplevel()
        self.highScore_frame.configure(bg="white")
        width = self.highScore_frame.winfo_screenwidth()
        height = self.highScore_frame.winfo_screenheight()
        self.highScore_frame.geometry("%dx%d" % (width, height))

        self.highScore_frame.geometry("%dx%d" % (width, height))
        self.highScore_frame.config(background="white")
        self.image = Image.open(self.IMAGE_PATH + "/highScoreBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.highScore_window = tk.Label(self.highScore_frame, image=self.background_image, justify='center')
        self.highScore_window.place(relwidth=1, relheight=1)

        #self.one_frame.attributes('-alpha', 0.5)

        self.one_frame = tk.Frame(self.highScore_window,bg="white")
        self.one_frame.pack(side=tk.LEFT,anchor="w", padx=175, pady=175)

        self.highScoreTitle_label = tk.Label(self.one_frame, text=" HIGH SCORE",bg="white")
        self.highScoreTitle_label.config(font=Font_tuple)
        self.highScoreTitle_label.pack(side=tk.TOP)
        self.highScoreValue_label = tk.Label(self.one_frame, text=self.highScore,bg="white")
        self.highScoreValue_label.config(font=Font_tuple)
        self.highScoreValue_label.pack()
        self.highScore_label = tk.Label(self.one_frame, text=self.currentScore,bg="white")
        self.highScore_label.config(font=smallFont_tuple)
        self.highScore_label.pack()

        play_fp = open(self.BASE_DIR + "/res/Images/play.png", "rb")
        play_photo = PIL.Image.open(play_fp)
        play_image = ImageTk.PhotoImage(play_photo)

        self.play_again_label = tk.Button(self.one_frame,image=play_image,bg="white",relief="flat",command=self.playAgain)
        self.play_again_label.pack(anchor='e')


        self.highScore_frame.mainloop()
    def playAgain(self):
        self.highScore_frame.destroy()


    def file_open_write(self,high_score):

        f = open(os.path.join(self.RESOURCE_PATH, 'File', 'high_score.txt'), 'w')
        f.truncate(0)
        f.write(high_score)
        f.close()
        return f


    def file_open_read(self):

        f = open(os.path.join(self.RESOURCE_PATH, 'File', 'high_score.txt'), 'r')
        best_score = f.read()
        print(best_score)
        return best_score


    def file_close(self,file):

        file.close()
