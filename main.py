
import os
import time
import random
from tkinter import Tk, Label, PhotoImage, CENTER

import settings


class DiceGame:
    """
    A simple dice game application using Tkinter.

    Methods:
        __init__(self):
            Initialize the DiceGame application.

        dice_roll(self) -> str:
            Simulate rolling a six-sided dice and return the corresponding dice icon filename.

        roll_dice(self, event) -> None:
            Simulate rolling two dice and update the displayed images during a roll animation.

        run(self) -> None:
            Start and run the DiceGame application.

    """

    def __init__(self):
        """
        Initialize the DiceGame application.

        Creates a Tkinter window with dice images, background, and user interaction setup.
        """
        captures_folder = os.path.join(os.path.dirname(__file__), settings.CAPTURES_FOLDER)
        self.icon_image = os.path.join(captures_folder, settings.DICE_ICON_NAME)
        self.background_image = os.path.join(captures_folder, settings.BACKGROUND_NAME)
        self.root = Tk()
        self.root.geometry(settings.SIZE_WINDOW)
        self.root.title(settings.WINDOW_TITLE)
        self.root.resizable(height=False, width=False)
        self.root.iconphoto(True, PhotoImage(file=self.icon_image))
        self.background = PhotoImage(file=self.background_image)

        Label(self.root, image=self.background).pack()
        self.label_1 = Label(self.root)
        self.label_1.place(relx=0.25, rely=0.5, anchor=CENTER)
        self.label_2 = Label(self.root)
        self.label_2.place(relx=0.75, rely=0.5, anchor=CENTER)

        self.root.bind('<1>', self.roll_dice)
        self.cube_1 = None
        self.cube_2 = None
        self.time_roll = None

        self.dice_images = [
            os.path.join(captures_folder, settings.DICE_1_ICON_NAME),
            os.path.join(captures_folder, settings.DICE_2_ICON_NAME),
            os.path.join(captures_folder, settings.DICE_3_ICON_NAME),
            os.path.join(captures_folder, settings.DICE_4_ICON_NAME),
            os.path.join(captures_folder, settings.DICE_5_ICON_NAME),
            os.path.join(captures_folder, settings.DICE_6_ICON_NAME),
        ]

    def dice_roll(self) -> str:
        """
        Simulate rolling a six-sided dice and return the corresponding dice icon filename.

        Returns:
            str: The filename of the dice icon representing the result of the dice roll.
        """
        return random.choice(self.dice_images)

    def roll_dice(self, event) -> None:
        """
        Simulate rolling two dice and update the displayed images during a roll animation.

        Args:
            event: An event object (e.g., button click event) that triggers the dice roll animation.

        """
        self.time_roll = 0.05
        for _ in range(settings.SCROLL_COUNT):
            self.cube_1 = PhotoImage(file=self.dice_roll())
            self.cube_2 = PhotoImage(file=self.dice_roll())
            self.label_1['image'] = self.cube_1
            self.label_2['image'] = self.cube_2
            self.root.update()
            time.sleep(self.time_roll)
            self.time_roll += settings.TIME_STEP

    def run(self) -> None:
        """
        Start and run the DiceGame application.
        """
        self.root.mainloop()


if __name__ == "__main__":
    game = DiceGame()
    game.run()
