import pygame
import sys
import random
import os

import time


from HighScore import HighScore



class GamePlay():
    def __init__(self,args):

        self.count = 0
        self.selected = args
        # Initialized resource path for cross platform compatibility
        self.BASE_DIR = os.path.dirname(__file__)
        self.RESOURCE_PATH = os.path.join(self.BASE_DIR, 'res')
        self.IMAGE_PATH = os.path.join(self.RESOURCE_PATH, 'Images')

        # Initializing pygame.

        pygame.init()
        # Initializing the width and height of the window to be 680 and 1250 pixels respectively.

        self.display_height = 680
        self.display_width = 1250

        # Setting the title and dimensions of the window

        pygame.display.set_caption('Train BRAIN')
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))

        pygame.mixer.music.load(os.path.join(self.RESOURCE_PATH, 'Songs', 'bgScore.wav'))
        pygame.mixer.music.play(-1)

        # Defining the clock to set the FPS rates
        self.clock = pygame.time.Clock()

        # Relatively small sized images to be placed in the main menu
        self.witch_image = pygame.image.load(os.path.join(self.IMAGE_PATH, 'ghost.png'))

        self.basket_image = pygame.image.load(os.path.join(self.IMAGE_PATH, 'basket.png'))

        if self.selected is "Fruits":

            self.object_images_raw = ['apple.png', 'bananas.png', 'grapes.jpg', 'orange.png', 'pineapple.jpg', 'strawberry.jpg',
                                'watermelon.jpg', 'chilli.png', 'mango.jpg', 'blueberry.jpg', 'cherries.jpg',
                                'halloween.png','avocado.jpg']
        elif self.selected is "Vegetables":
            self.object_images_raw = ['tomato.png', 'beet.png', 'carrot.png', 'cucumber.png', 'eggplant.png',
                                      'potato.png',
                                      'spinach.png', 'chilli.png', 'garlic.png', 'halloween.png', 'cauliflower.png',
                                      'corn.png','okra.png']
        elif self.selected is "Animals":
            self.object_images_raw = ['cow.png', 'sheep.png', 'dog.png', 'lion.png', 'giraffe.png',
                                      'elephant.png',
                                      'horse.png', 'chicken.png', 'pig.png', 'tiger.png', 'zebra.png',
                                      'cat.png']
        elif self.selected is "Numbers":
            self.object_images_raw = ['one.jpg', 'two.jpg', 'three.jpg', 'lion.png', 'giraffe.png',
                                      'four.jpg',
                                      'five.png', 'six.png', 'seven.png', 'eight.jpg', 'nine.jpg',
                                      'ten.png']
        self.object_images = [os.path.join(self.IMAGE_PATH, i) for i in self.object_images_raw]

        self.bomb_image = pygame.image.load(self.object_images[7])

        self.basket = pygame.image.load(os.path.join(self.IMAGE_PATH, 'basket.png'))

        self.minion = pygame.image.load(self.object_images[11])

        self.explosion = pygame.image.load(os.path.join(self.IMAGE_PATH, 'ghost.png'))

        # Initializing the speed variable which denotes the speed with which the images move.

        self.image_speed = 3

        # Intialiaing the score variable.

        self.score = 0

        # Pixels being moved by the basket under keystrokes (10 px)

        self.unit = 4

        self.user_clicked = False

        # Setting white background to the game window
        self.gameDisplay.fill((255, 255, 255))

        # X and Y co-ordinates of the basket.
        self.basket_x = self.display_width / 2 - 200

        self.basket_y = self.display_height - 270

        # For changing the X co-ordinate of the basket when appropriate keys are pressed.
        self.x_change = 0

        # Random positions for fruits

        self.x = random.randint(0, self.display_width - 250)
        self.y = -150

        # Randomly loading fruit images

        self.random_images = self.object_images[random.randint(0, 12)]

        self.random_fruits = pygame.image.load(self.random_images)


    def setText(self,text, font_size, position, foreground_color, background_color=None, font_family="Times New Roman"):
        # Setting the font and related font features as per the parameters supplied.

        font = pygame.font.SysFont(font_family, font_size)
        text_to_display = font.render(text, 1, foreground_color, background_color)
        self.gameDisplay.blit(text_to_display, position)
        pygame.display.update()

    # Defining functions for file operations.


    def file_open_write(self,high_score):

        f = open(os.path.join(self.RESOURCE_PATH, 'File', 'high_score.txt'), 'w')
        f.write(high_score)
        return f


    def file_open_read(self):

        f = open(os.path.join(self.RESOURCE_PATH, 'File', 'high_score.txt'), 'r')
        best_score = f.read()
        return f, best_score


    def file_close(self,file):

        file.close()

    def play(self):
        self.play_clicked = True
        while self.play_clicked:

            # New game window is created on clicking the play button with the same dimensions.
            self.play_window = pygame.display.set_mode((1250, 680))

            pygame.display.set_caption('Play')

            self.play_window.fill((255, 255, 255))

            self.play_clock = pygame.time.Clock()

            self.play_window.blit(self.random_fruits, (self.x, self.y))



            # Horizontal line carrying the basket.

            pygame.draw.line(self.play_window, (175, 115, 0), (0, self.display_height - 20), (self.display_width, self.display_height - 20))

            # Color beneath the line.

            pygame.draw.rect(self.play_window, (243, 128, 12), (0, self.display_height - 18, self.display_width, self.display_height))

            for self.event in pygame.event.get():

                # Event handling
                if self.event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                elif self.event.type == pygame.KEYDOWN:

                    if self.event.key == pygame.K_RIGHT:

                        self.x_change = self.unit

                    elif self.event.key == pygame.K_LEFT:

                        self.x_change = -self.unit

                    elif self.event.key == pygame.K_DOWN:

                        self.x_change = 0

            self.basket_x += self.x_change

            self.y += self.image_speed

            # Placing the Basket in position

            self.play_window.blit(self.basket, (self.basket_x, self.basket_y))



            # Placing score on the game window.

            self.setText("You collected "+str(self.count)+" items and Your Score is " + str(self.score), 40, (0, 0), (107, 20, 99), (128, 255, 255))

            # Checking fruit and basket crossover.

            if self.y + 80 >= self.basket_y and self.y + 80 <= self.basket_y + 15:

                if self.x >= self.basket_x - 40 and self.x + 100 <= self.basket_x + self.display_width / 2 - 240:

                    # Checks collision with bomb and minion image

                    if self.random_images == self.minion or self.random_images == self.object_images[7]:

                        self.score -= 5
                        self.setText("Your Score:" + str(self.score), 40, (0, 0), (107, 20, 99), (128, 255, 255))

                        # Checking whether the current score is greater than the best score.

                        self.file, self.current_best_score = self.file_open_read()

                        self.file_close(self.file)

                        #if self.score > int(self.current_best_score):
                            #self.file = self.file_open_write(str(self.score))
                            #self.file_close(self.file)

                        self.setText("Crashed", 150, (self.display_width / 2 - 240, 35), (0, 0, 0))
                        self.setText(None, 40, (0, 0), (255, 255, 255))
                        self.play_window.blit(self.explosion, (self.basket_x, self.basket_y - 80))
                        pygame.display.update()

                        time.sleep(3)

                        for k in range(0, self.display_width + 1, 5):
                            self.setText("Your Score:" + str(self.score), 40, (k, 0), (107, 20, 99), (128, 255, 255))
                            pygame.time.wait(20)

                        time.sleep(2)

                        pygame.quit()
                        highScore = HighScore(self.score,self.count)
                        break

                        #game_over = True
                        #play_clicked = False


                    # Makes the fruit disappear !

                    self.y = self.display_height

                    # Incrementing the score appropriately.

                    if self.random_images == self.object_images[6]:

                        self.count += 1
                        self.score += 1

                    elif self.random_images == self.object_images[0] or self.random_images == self.object_images[1] or self.random_images == self.object_images[3]:
                        self.count += 1
                        self.score += 3

                    elif self.random_images == self.object_images[4] or self.random_images == self.object_images[5] or self.random_images == self.object_images[8]:
                        self.count += 1
                        self.score += 5

                    elif self.random_images == self.object_images[2]:
                        self.count += 1
                        self.score += 10

            # Checking whether the fruit image had crossed the floor.

            if self.y >= self.display_height + 200:

                # Random positions for fruits

                self.x = random.randint(0, self.display_width - 250)
                self.y = -150

                # Randomly loading fruit images

                self.random_images = self.object_images[random.randint(0, 9)]

                self.random_fruits = pygame.image.load(self.random_images)

                # Increasing the speed in which the basket moves both the directions.

                if self.score > 75:
                    self.unit += 1

                # Increasing the speed in which the images moves down.

                if self.score > 75:
                    self.image_speed += 0.5

            # Restricting the basket within the width of the Game window

            if self.basket_x <= 0:

                self.basket_x = 0

            elif self.basket_x >= self.display_width - 300:

                self.basket_x = self.display_width - 300

            pygame.display.update()
            self.play_clock.tick(60)
    def setEvent(self,gestureEvent):
        self.event = gestureEvent
