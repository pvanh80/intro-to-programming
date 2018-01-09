
from tkinter import *
import random


DICEPICS = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif" ]

class UserInferface:

    def __init__(self):

        self.main_window = Tk()

        self.__dicepics = []
        for image_file in DICEPICS:
            pic = PhotoImage(file=image_file)
            self.__dicepics.append(pic)

        self.__dice1Label = Label(self.main_window)
        self.__dice1Label.grid(row=2, column=0)

        self.__dice1Label.configure(image=self.__dicepics[0])

        self.__throwButton = Button(self.main_window, text="throw", command=self.throw).grid(row=0, column=2, columnspan=2, sticky=E)

        self.main_window.mainloop()

    def throw(self):
        self.__dice1Label.configure(image=self.__dicepics[random.randint(0,5)])


def main():
        my = UserInferface()
main()