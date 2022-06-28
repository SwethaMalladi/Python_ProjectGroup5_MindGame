import tkinter as tk
import os
import PIL
from PIL import ImageTk, Image



class Instructions:


    def __init__(self, args=None):

        self.BASE_DIR = os.path.dirname(__file__)
        self.RESOURCE_PATH = os.path.join(self.BASE_DIR, 'res')
        self.IMAGE_PATH = os.path.join(self.RESOURCE_PATH, 'Images')

        self.BASE_DIR = os.path.dirname(__file__)
        Font_tuple = ("Comic Sans MS", 40)
        smallFont_tuple = ("Comic Sans MS", 20)

        # Create main Window
        self.instruction_frame = tk.Toplevel()
        self.instruction_frame.configure(bg="white")
        width = self.instruction_frame.winfo_screenwidth()
        height = self.instruction_frame.winfo_screenheight()
        self.instruction_frame.geometry("%dx%d" % (width, height))

        self.instruction_frame.geometry("%dx%d" % (width, height))
        self.instruction_frame.config(background="white")
        self.image = Image.open(self.IMAGE_PATH + "/rulesBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.instruction_window = tk.Label(self.instruction_frame, image=self.background_image, justify='center')
        self.instruction_window.place(relwidth=1, relheight=1)


        self.rule_frame = tk.Frame(self.instruction_window, bg="white")
        self.rule_frame.pack(side=tk.TOP, anchor="w", padx=310, pady=220)

        self.ruleTitle_label = tk.Label(self.rule_frame,text="Rules...",bg="white")
        self.ruleTitle_label.config(font=Font_tuple)
        self.ruleTitle_label.pack()
        self.rule1_label = tk.Label(self.rule_frame, text="1. Use left and right arrow keys to move the basket appropriately.",bg="white",justify="left")
        self.rule1_label.config(font=smallFont_tuple)
        self.rule1_label.pack(anchor='w')
        self.rule2_label = tk.Label(self.rule_frame, text="2. Use down arrow key to stop the basket at that point.",bg="white",justify="left")
        self.rule2_label.config(font=smallFont_tuple)
        self.rule2_label.pack(anchor='w')
        self.rule3_label = tk.Label(self.rule_frame, text="3. Collect as many objects as you can with the basket.",bg="white",justify="left")
        self.rule3_label.config(font=smallFont_tuple)
        self.rule3_label.pack(anchor='w')
        self.rule4_label = tk.Label(self.rule_frame, text="4. Avoid crashing with odd object!",bg="white",justify="left")
        self.rule4_label.config(font=smallFont_tuple)
        self.rule4_label.pack(anchor='w')
        self.rule5_label = tk.Label(self.rule_frame, text="5. Points Awarded: 1, 3, 5 and 10 depending up on the kind of objects.", bg="white",justify="left")
        self.rule5_label.config(font=smallFont_tuple)
        self.rule5_label.pack(anchor='w')

        # self.one_frame.attributes('-alpha', 0.5)

        self.back_frame = tk.Frame(self.rule_frame, bg="white")
        self.back_frame.pack(side=tk.BOTTOM, anchor="e")

        back_fp = open(self.BASE_DIR + "/res/Images/back.png", "rb")
        back_photo = PIL.Image.open(back_fp)
        back_image = ImageTk.PhotoImage(back_photo)

        self.back_label = tk.Button(self.back_frame, image=back_image, bg="white", relief="flat",
                                          command=self.backAgain)
        self.back_label.pack(side=tk.RIGHT)

        self.instruction_window.mainloop()

    def backAgain(self):
        self.instruction_frame.destroy()
