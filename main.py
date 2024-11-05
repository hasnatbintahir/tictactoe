import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.turn_label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=('normal', 20, 'bold'))
        self.turn_label.grid(row=0, column=0, columnspan=3)
        
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 40, 'bold'), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=(i//3) + 1, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.buttons[index].cget("text") == "" and not self.check_winner():
            self.buttons[index].config(text=self.current_player)
            self.board[index] = self.current_player
            winning_combo = self.check_winner()
            if winning_combo:
                for i in winning_combo:
                    self.buttons[i].config(bg="green")
                self.turn_label.config(text=f"Player {self.current_player} wins!")
                self.root.after(2000, self.reset_game)  # Delay reset to allow players to see the winning line
            elif "" not in self.board:
                self.turn_label.config(text="It's a tie!")
                self.root.after(2000, self.reset_game)  # Delay reset for 2 seconds
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return combo
        return None

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")  # Reset text and background color
        self.current_player = "X"
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
