from tkinter import *
import random

def next_turn():
    pass


def check_winner():
    pass


def empty_spaces():
    pass


def new_game():
    pass


window = Tk()                               # Initialize Window
window.title("Tic Tac Toe")                 # Name of the window
players = ["X", "O"]                        # Players 
player = random.choice(players)             # First Moves random...
buttons = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]                       # 2D List (TABLE)
          
label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

restart_button = Button(text="Restart", font=("Consolas", 20), command=new_game)
restart_button.pack(side="top")

frame = Frame(master=window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(master=frame, text="")

window.mainloop()