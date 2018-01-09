from tkinter import *
from tkinter import ttk
import random
#from demopanels import MsgPanel, SeeDismissPanel

# http://pyinmyeye.blogspot.fi/2012/07/tkinter-15-puzzle-demo-placer-geometry.html

NUM_ROWS = 5 # number of rows and column
PLAYER_NUMBER = 2
PLAY_TURNS = 2
DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17,18,19,20,21,22,23,24] # button text value
random.shuffle(DATA)


class PuzzleDemo(Frame):
    def __init__(self, name='puzzledemo'):
        Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)

        self.master.title('15 Puzzle Demo')
        self.master.maxsize(int(NUM_ROWS*100),int(NUM_ROWS*100))
        self.master.minsize(int(NUM_ROWS* 100), int(NUM_ROWS* 100))
        self._create_demo_panel()

    def _create_demo_panel(self):
        bgColor = 'gray'  # colour for panel background and empty space
        bgInfo = "PINK"
        # if width and height are not specifically set buttons are positioned
        # in a 0 size window and do not show up
        demoPanel = Frame(self,background=bgColor,width=NUM_ROWS/2*100, height=NUM_ROWS/2*100)

        demoInfo = Frame(self, background=bgInfo, width=150, height=NUM_ROWS*100)

        demoPanel.pack(side=LEFT, padx=1)
        demoInfo.pack(side=LEFT)
        # demoPanel.grid(row=1,column=1)
        # demoInfo.grid(row=2,column=1)

        # buttons are placed relative to the top, left corner of demoPanel
        # with relations expressed as a value between 0.0 and 1.0
        # top, left corner = (x,y) = (0,0)
        # bottom, right corner = (x,y) = (1,1)
        self.xyposition = {}
        self.xyposition['space'] = ((NUM_ROWS - 1) * 0.25, (NUM_ROWS - 1) * 0.25)

        for i in range(len(DATA)):
            num = DATA[i]
            self.xyposition[num] = (i % NUM_ROWS * .25, i // NUM_ROWS * .25)
            b = ttk.Button(text=num, style='Puzzle.TButton')
            b['command'] = lambda b=b: self._puzzle_switch(b)
            b.place(in_=demoPanel, relx=self.xyposition[num][0], rely=self.xyposition[num][1],
                    relwidth=.25, relheight=.25)


        #display
        self.score = StringVar(value=0)

        self.score_text = ttk.Label(demoInfo,textvariable=self.score, style='Puzzle.Label')
        self.score_moved_text = ttk.Label(demoInfo,text="Moved: ", style='Puzzle.Label')

        #self.score_text.place(in_=demoInfo, relx=0.4, rely=0, relwidth=.7, relheight=.1)
        #self.score_moved_text.place(in_=demoInfo, relwidth=.4, relheight=.1)
        # self.score_moved_text.pack(side=RIGHT)
        # self.score_text.pack(side=RIGHT)

        # set button background to demoPanel background
        ttk.Style().configure('Puzzle.TButton', background=bgColor, font=('Helvetica', 13))
        ttk.Style().configure('Puzzle.Label', background=bgInfo,
                              font=('Helvetica', 13))


    def _puzzle_switch(self, button):
        num = button['text']
        sx = self.xyposition['space'][0]  # position of 'space'
        sy = self.xyposition['space'][1]
        x = self.xyposition[num][0]  # position of selected button
        y = self.xyposition[num][1]

        # is the selected button next to the space?
        if (sy - .01 <= y <= sy + .01 and sx - .26 <= x <= sx + .26
            or sx - .01 <= x <= sx + .01 and sy - .26 <= y <= sy + .26):
            # swap button with space
            self.xyposition['space'], self.xyposition[num] = self.xyposition[num], self.xyposition['space']

            # re-position button
            button.place(relx=self.xyposition[num][0], rely=self.xyposition[num][1])

            current_score = int(self.score.get())
            current_score += 1
            self.score.set(str(current_score))

if __name__ == '__main__':
    PuzzleDemo().mainloop()