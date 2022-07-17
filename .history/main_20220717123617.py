from tkinter import *
import random


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
            # change the color to show we have a winner
            buttons[row][0].config(bg="#32a302")
            buttons[row][1].config(bg="#32a302")
            buttons[row][2].config(bg="#32a302")
            return True

    # We will check all of the vertical conditions
    for column in range(3):
        # if every vertical buttons is equal and not empty
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # change the color to show we have a winner
            buttons[0][column].config(bg="#32a302")
            buttons[1][column].config(bg="#32a302")
            buttons[2][column].config(bg="#32a302")
            return True
    
    # Now, we're gonna check diagonals conditions, and return True, if the conditions are true
    # Main's Diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # change the color to show we have a winner
        buttons[0][0].config(bg="#32a302")
        buttons[1][1].config(bg="#32a302")
        buttons[2][2].config(bg="#32a302")
        return True
    # Secondary's Diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # change the color to show we have a winner
        buttons[0][2].config(bg="#32a302")
        buttons[1][1].config(bg="#32a302")
        buttons[2][0].config(bg="#32a302")
        return True
    # If empty spaces returns False, meaning that we dont have empty spaces, return tie...
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='#c6db07', fg="#000000")
        return "Tie"
    else:
        # if any conditions are True, returns False because we don't have a winner yet.
        return False

    
def empty_spaces():
    # We have 9 slots in tic-tac-toe game
    spaces = 9
    # if the row/column that we checking it's not empty... we take minus 1 from the empty spaces left
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    # if remains 0 empty spaces return False
    if spaces == 0:
        return False
    # else, return True..
    else:
        return True


def new_game():
    # define global that we can have access and change the player
    global player
    # player receive another random choice
    player = random.choice(players)
    # and then the label receive the turn of the choosed player
    label.config(text=(player + " turns"))
    # and finally, we empty the buttons...
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",
                                        bg="#000000",
                                        fg="#ffffff")



window = Tk()                               # Initialize Window
window.resizable(width=False, height=False)
window.config(bg="#000000") #fg="#ffffff")
window.title("Tic Tac Toe")                 # Name of the window
players = ["X", "O"]                        # Players 
player = random.choice(players)             # First Moves random...
buttons = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]                       # 2D List (TABLE)

# label showing messages (winner or TIE)
label = Label(text=player + " turn", font=("consolas", 30))
label.pack(side="top")
# restart button 
restart_button = Button(text="Restart", font=("Consolas", 20), command=new_game)
restart_button.pack(side="top")
# frame that we have buttons
frame = Frame(master=window)
frame.pack()
# buttons in the frame
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(master=frame, 
                                      text="", 
                                      font=("consolas", 40), 
                                      width=3, 
                                      height=1,
                                      command= lambda row=row, column=column: next_turn(row, column),
                                      fg="#ffffff",
                                      bg="#000000")
        buttons[row][column].grid(row=row, column=column)                      

window.mainloop()