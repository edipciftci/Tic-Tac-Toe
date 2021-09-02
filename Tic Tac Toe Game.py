import tkinter as tk
from tkinter import font as tkFont
import json

def start():
    
    # This function starts the game
    
    # Game window initiation 
    
    root = tk.Tk()
    root.geometry("600x600")
    root.resizable(False, False)
    
    # Theme assignment
    
    with open('themes.json', 'r') as f:
        theme = json.load(f)
    
    bg_color = theme[2]["bg_color"]
    frame_color = theme[2]["frame_color"]
    fg_color = theme[2]["fg_color"]

    def game():
        
        # Main function to run the game. 
        # Game logic and GUI are both in this function.
        
        # Table array keeps what each cell holds.
        # Necessary for the game logic.
        
        table = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
        
        def check_full_table():
            
            # Function to determine if the table is full.
            # This function will only be called after check_winner() returns false.
            # Therefore, if it returns true that means the game has ended in a draw.
            
            for cell in table:
                if cell == " ":
                    return False
            return True
        
        def check_winner():
            
            # Function to determine if any side has won.
            # Returns 'X' or 'O' or 'None'
            
            def check_row():
                
                # Determines if there is a winner based on the rows.
                
                for i in range(0, 9, 3):
                    if table[i] == " ":
                        continue
                    elif table[i] == table[i + 1] == table[i + 2]:
                        return table[i]
                    
            def check_col():
                
                # Determines if there is a winner based on the columns.
                
                for i in range(0, 3):
                    if table[i] == " ":
                        continue
                    elif table[i] == table[i + 3] == table[i - 3]:
                        return table[i]
                    
            def check_diagonal():
                
                # Determines if there is a winner based on the diagonals.
                
                if table[0] != " ":
                    if table[0] == table[4] == table[8]:
                        return table[0]
                if table[2] != " ":
                    if table[2] == table[4] == table[6]:
                        return table[2]
            
            if check_row() is not None:
                return check_row()
            elif check_col() is not None:
                return check_col()
            elif check_diagonal() is not None:
                return check_diagonal()
        
        def stop_func():
            
            # Function to end the game if one side wins and/or there is no logical moves left.
            
            winner = check_winner()
            if winner is not None:
                print(winner + " is the winner!")
            elif check_full_table():
                print("There is a tie!")
                
            # TODO: Endgame widget
        
        def count_moves():
            
            # Counts the played moves to help determining the turns.
            
            count = 0
            for string in table:
                if string == " ":
                    pass
                else:
                    count += 1
            return int(count)
        
        def modify_table(num: int):
            
            # Function to implement the necessary adjustments on the table array based on the last move.
            # Uses count_moves() to determine the turn.
            
            if count_moves() % 2:
                table[num] = "O"
            else:
                table[num] = "X"
            print(table)
        
        def text_change(bttn: tk.Button):
            
            # Function to implement the necessary adjustments on the last played cell based on the last move.
            
            if count_moves() % 2:
                bttn.configure(text="O")
            else:
                bttn.configure(text="X")
        
        def click(bttn: tk.Button, num: int):
            
            # Makes a move when a button is clicked, if it is legal.
            # Uses necessary functions to adjust the game logic and GUI based on the move.
            # Checks if the game has ended.
            
            if(table[num] == " "):
                text_change(bttn)
                modify_table(num)
                stop_func()        
        
        def button_creation():
            
            # Function to create the cells.
            
            top_left = tk.Button(frame, bg=bg_color, text=table[0],
                                 command=lambda: click(top_left, 0))
            top_center = tk.Button(frame, bg=bg_color, text=table[1],
                                   command=lambda: click(top_center, 1))
            top_right = tk.Button(frame, bg=bg_color, text=table[2],
                                  command=lambda: click(top_right, 2))
            mid_left = tk.Button(frame, bg=bg_color, text=table[3],
                                 command=lambda: click(mid_left, 3),)
            mid_center = tk.Button(frame, bg=bg_color, text=table[4],
                                   command=lambda: click(mid_center, 4))
            mid_right = tk.Button(frame, bg=bg_color, text=table[5],
                                  command=lambda: click(mid_right, 5))
            bottom_left = tk.Button(frame, bg=bg_color, text=table[6],
                                    command=lambda: click(bottom_left, 6))
            bottom_center = tk.Button(frame, bg=bg_color, text=table[7],
                                      command=lambda: click(bottom_center, 7))
            bottom_right = tk.Button(frame, bg=bg_color, text=table[8],
                                     command=lambda: click(bottom_right, 8))

            buttons = [top_left, top_center, top_right,
                       mid_left, mid_center, mid_right,
                       bottom_left, bottom_center, bottom_right]
            
            a = 0.01
            default_font = tkFont.Font(family="Helvetica", size=50, weight="bold") 
            
            for btn in buttons:
                btn.config(font=default_font)
                btn.configure(fg=fg_color)
                
            # Cell placement

            top_left.place(relx=2 * a, rely=2 * a, relwidth=30 * a, relheight=30 * a)
            top_center.place(relx=35 * a, rely=2 * a, relwidth=30 * a, relheight=30 * a)
            top_right.place(relx=68 * a, rely=2 * a, relwidth=30 * a, relheight=30 * a)
            mid_left.place(relx=2 * a, rely=35 * a, relwidth=30 * a, relheight=30 * a)
            mid_center.place(relx=35 * a, rely=35 * a, relwidth=30 * a, relheight=30 * a)
            mid_right.place(relx=68 * a, rely=35 * a, relwidth=30 * a, relheight=30 * a)
            bottom_left.place(relx=2 * a, rely=68 * a, relwidth=30 * a, relheight=30 * a)
            bottom_center.place(relx=35 * a, rely=68 * a, relwidth=30 * a, relheight=30 * a)
            bottom_right.place(relx=68 * a, rely=68 * a, relwidth=30 * a, relheight=30 * a)
    
        frame = tk.Frame(root, bg=frame_color)
        frame.place(relwidth=1, relheight=1)
        
        button_creation()
    
    game()
    root.mainloop()
    
start()
