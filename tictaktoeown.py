import tkinter as tk


def set_tile(row,column):
    global current_player
    if game_over:
        return
    if (board[row][column]["text"] != ""):
        return
    board[row][column]["text"] = current_player
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO
    label["text"] = f"{current_player}'s turn!" 
    check_winner()


def check_winner():
    global turns,game_over
    turns += 1
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "" ):
            label.config(text=f"""{board[row][0]["text"]} Won""", foreground=color_yellow, background=color_grey )
            for column in range(3):
                board[row][column].config(foreground= color_yellow, background=color_light_grey)
                game_over = True
            return
             
                 
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "" ):
            label.config(text=f"""{board[0][column]["text"]} Won""", foreground=color_yellow, background=color_grey )
            for row in range(3):
                board[row][column].config(foreground= color_yellow, background=color_light_grey)
                game_over = True
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "" ):
        label.config(text=f"""{board[0][0]["text"]} Won""", foreground=color_yellow, background=color_grey )
        board[0][0].config(foreground= color_yellow, background=color_light_grey)
        board[1][1].config(foreground= color_yellow, background=color_light_grey)
        board[2][2].config(foreground= color_yellow, background=color_light_grey)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "" ):
        label.config(text=f"""{board[0][0]["text"]} Won""", foreground=color_yellow, background=color_grey )
        board[0][2].config(foreground= color_yellow, background=color_light_grey)
        board[1][1].config(foreground= color_yellow, background=color_light_grey)
        board[2][0].config(foreground= color_yellow, background=color_light_grey)
        game_over = True
        return
    
    
    if turns == 9:
        label.config(text=f"It was a Tie!", foreground="#ffffff", background=color_grey )
        return

def new_game():
    global turns,game_over
    
    game_over = False
    turns = 0
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_grey)
            label.config(text=f"{current_player}'s Turn!", font=("Roboto", 20, "bold"), background=color_grey, foreground="#ffffff")

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

game_over = False
turns = 0
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"


playerX = "X"
playerO = "O"

current_player = playerX
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
frame = tk.Frame(window)
label = tk.Label(frame, text=f"{current_player}'s Turn!", font=("Roboto", 20, "bold"), background=color_grey, foreground="#ffffff")
label.grid(row=0, column=0, columnspan=3, sticky="we")


for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame,text="", font=("consolas", 40, "bold"), width=5, height=2,
                                       command= lambda row=row, column=column: set_tile(row,column), foreground=color_blue, background=color_grey)
        board[row][column].grid(row=row+1, column=column)


reset_button = tk.Button(frame, text="Restart", font=("nunito", 20), foreground="#ffffff", background=color_grey, command=new_game)
reset_button.grid(row=4,column=0,columnspan=3, sticky="we")

frame.pack()
window.update()
window.mainloop()