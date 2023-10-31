from tkinter import *
import random
import time


def dice_roll():
    return random.choice([
        '1.png', '2.png',
        '3.png', '4.png',
        '5.png', '6.png',
    ])


def img(event):
    global cube_1, cube_2
    cube_1 = PhotoImage(file=dice_roll())
    cube_2 = PhotoImage(file=dice_roll())
    label_1['image'] = cube_1
    label_2['image'] = cube_2


def main():
    global label_1, label_2
    global cube_1, cube_2
    root = Tk()
    root.geometry('400x200')
    root.title('Dice game! Take a shot!')
    root.resizable(height=False, width=False)
    root.iconphoto(True, PhotoImage(file='3.png'))
    background = PhotoImage(file='background.png')
    Label(root, image=background).pack()
    label_1 = Label(root)
    label_1.place(relx=0.25, rely=0.5, anchor=CENTER)
    label_2 = Label(root)
    label_2.place(relx=0.75, rely=0.5, anchor=CENTER)
    root.bind('<1>', img)

    root.mainloop()


if __name__ == '__main__':
    main()
