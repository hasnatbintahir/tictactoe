import tkinter as tk
from tkinter import messagebox

def set_tile(row, column):
    global current_player
    
    if (game_over):
        return
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = current_player
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO
    label["text"] = current_player+"'s turn" 
    check_winner()

def check_winner():
    
    global turns,game_over
    
    turns += 1
    #checking horizontally
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + "is the winner!", foreground=color_yellow, background=color_grey )
            for column in range(3):
                board[row][column].config(foreground= color_yellow, background=color_light_grey)
            game_over = True
            return
        
    #check vertically
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + "is the winner!", foreground=color_yellow, background=color_grey )
            for row in range(3):
                board[row][column].config(foreground= color_yellow, background=color_light_grey)
            game_over = True
            return
        
    #check digonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + "is the winner!", foreground=color_yellow, background=color_grey )
        for row in range(3):
                board[row][row].config(foreground= color_yellow, background=color_light_grey)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][0]["text"] + "is the winner!", foreground=color_yellow, background=color_grey )
        board[0][2].config(foreground= color_yellow, background=color_light_grey)
        board[1][1].config(foreground= color_yellow, background=color_light_grey)
        board[2][0].config(foreground= color_yellow, background=color_light_grey)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        label.config(text="Its a tie!")
        game_over = True
        return
        

def new_game():
    global turns, game_over
    
    turns = 0
    game_over = False
    
    label.config(text= current_player+"'s turn!", foreground="white", background=color_grey)
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground = color_blue, background = color_grey)


turns = 0
game_over = False
playerX = "X"
playerO = "O"
current_player = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"

window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)

label = tk.Label(frame, text=f"{current_player}'s turn" , font=("Consolas", 20),foreground="white", background=color_grey )
label.grid(row=0, column=0, columnspan=3, sticky="we")


for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Consolas", 40, "bold"), width=7,height=3,
                                       command=lambda row = row, column = column: set_tile(row,column),foreground=color_blue, background=color_grey)
        board[row][column].grid(row=row+1, column=column)


reset_button = tk.Button(frame, text="Restart", foreground="white", background=color_grey, font=("consolas", 20), command=new_game)

reset_button.grid(row=4,column=0, columnspan=3, sticky="we")

frame.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()                

