from tkinter import *
import random

from pyparsing import col

def next_turn(row, column):
    # global player to have access 
    global player
    # if text in the button equals "None" and Check winner returns false...
    if buttons[row][column]["text"] == "" and check_winner() is False:
        # if player in te list players in position 0, that means "X"
        if player == players[0]:
            # button text receive the player move "X"
            buttons[row][column]["text"] = player
            # if check winner returns false agains (meaning that we don't have winner yet..)
            if check_winner() is False:
                # we swap players, taking the position 1 from the player list, meaning "O"
                player = players[1]
                # and we show in the window... the player's turn.
                label.config(text=players[1] + " turn")
            # else if check winner returns true (meaning the "X" won the game)
            elif check_winner() is True:
                # show in the window... "X wins"
                label.config(text=(players[0] + " wins!"))
            # check if we have a Tie
            elif check_winner() == "Tie":
                # show in the window that we have a TIE..."
                label.config(text=("It's a TIE!"))
        # if player not "X", means "O"      
        else:
            # button text receive the player move "O"
            buttons[row][column]["text"] = player
            # if check winner returns false agains (meaning that we don't have winner yet..)
            if check_winner() is False:
                # we swap players, taking the position 0 from the player list, meaning "X"
                player = players[0]
                # and we show in the window... the player's turn.
                label.config(text=players[0] + " turn")
            # else if check winner returns true (meaning the "O" won the game)
            elif check_winner() is True:
                # show in the window... "O wins"
                label.config(text=(players[1] + " wins!"))
            # check if we have a Tie
            elif check_winner() == "Tie":
                # show in the window that we have a TIE..."
                label.config(text=("It's a TIE!"))     


def check_winner():
    # We will check all of the horizontal conditions
    for row in range(3):
        # if every horizontal buttons is equal and not empty
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    # We will check all of the vertical conditions
    for column in range(3):
        # if every vertical buttons is equal and not empty
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
    
    # Now, we're gonna check diagonals conditions, and return True, if the conditions are true
    # Main's Diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    # Secondary's Diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    # If empty spaces returns False, meaning that we dont have empty spaces, return tie...
    elif empty_spaces() is False:
        return "Tie"
    else:
        # if any conditions are True, returns False because we don't have a winner yet.
        return False

    
def empty_spaces():
    # We have 9 slots in tic-tac-toe game
    spaces = 9
    # if the row/column that we checking it's not empty... 
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


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