
import os
import time
import random
from tkinter import Tk, Label, PhotoImage, CENTER


class DiceGame:
    """
    A simple dice game application using Tkinter.

    Attributes:
        TIME_STEP (float): The time delay between updating dice images during the roll animation.
        SCROLL_COUNT (int): The number of times dice images are updated during the roll animation.

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
    TIME_STEP = 0.05
    SCROLL_COUNT = 9

    def __init__(self):
        """
        Initialize the DiceGame application.

        Creates a Tkinter window with dice images, background, and user interaction setup.
        """
        captures_folder = os.path.join(os.path.dirname(__file__), 'Captures')
        self.icon_image = os.path.join(captures_folder, 'dice-icon.png')
        self.background_image = os.path.join(captures_folder, 'background.png')
        self.root = Tk()
        self.root.geometry('400x200')
        self.root.title('Dice game! Take a shot!')
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
            os.path.join(captures_folder, 'dice-1-icon.png'),
            os.path.join(captures_folder, 'dice-2-icon.png'),
            os.path.join(captures_folder, 'dice-3-icon.png'),
            os.path.join(captures_folder, 'dice-4-icon.png'),
            os.path.join(captures_folder, 'dice-5-icon.png'),
            os.path.join(captures_folder, 'dice-6-icon.png'),
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
        for _ in range(self.SCROLL_COUNT):
            self.cube_1 = PhotoImage(file=self.dice_roll())
            self.cube_2 = PhotoImage(file=self.dice_roll())
            self.label_1['image'] = self.cube_1
            self.label_2['image'] = self.cube_2
            self.root.update()
            time.sleep(self.time_roll)
            self.time_roll += self.TIME_STEP

    def run(self) -> None:
        """
        Start and run the DiceGame application.
        """
        self.root.mainloop()


if __name__ == "__main__":
    game = DiceGame()
    game.run()
