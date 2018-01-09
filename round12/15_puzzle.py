from tkinter import *
import tkinter.messagebox
import random

NUM_ROWS = 4 # number of rows and column
DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # button text value
random.shuffle(DATA)

class UserInterface:

    def __init__(self):

        self.__main_window = tkinter.Tk()
        self.__main_window.title("15 puzzle")
        self.__button = []
        self.__row_button = []
        for col in range(0,NUM_ROWS):
            for row in range(0, NUM_ROWS):
                if col ==3 and row==3:
                    self.__row_button= tkinter.Label(self.__main_window,text="",
                                                       height=2,width=5, bg="red").grid(row= row,column=col)
                else:

                    self.__row_button.append(tkinter.Button(self.__main_window, text=str(DATA.pop()),
                                                        height=2,width=5, command=lambda row=row, column=col:
                                                        self.switch_value(row, column)).grid(row=row, column=col))
            self.__button.append(self.__row_button)


        # map button on the maindow

    def start(self):
        self.__main_window.mainloop()

    def switch_value(self, row, column):
        #if row - 1 < 0 and column - 1 < 0:
            #tkinter.messagebox.showinfo("Info", "row="+str(row) + " col="+str(column))
            #self.__button[column][row] = tkinter.Label(self.__main_window,text="AAA", height=2,width=5, bg="red").grid(row= row,column=column)
        return
def main():
    myUI = UserInterface()
    myUI.start()
    print(DATA)
main()