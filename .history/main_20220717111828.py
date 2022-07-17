from tkinter import *
import random

def next_turn(row, column):
    # global player to have access 
    global player
    # if text in the button equals "None" and Check winner returns false...
    if buttons[row][column]["text"] == "" and check_winner() is False:
        # if player in te list players 
        if player == players[0]:
            
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=players[1] + " turn")


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
        buttons[row][column] = Button(master=frame, 
                                      text="", 
                                      font=("consolas", 40), 
                                      width=5, 
                                      height=2,
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)                      

window.mainloop()