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
        
        def stop_func():
            
            # Function to end the game if one side wins and/or there is no logical moves left.
            
            pass
        
        def modify_table(num: int):
            
            # Function to implement the necessary adjustments on the table array based on the last move.
            
            pass
        
        def text_change(bttn: tk.Button):
            
            # Function to implement the necessary adjustments on the last played cell based on the last move.
            
            pass
        
        def button_creation():
            
            # Function to create the cells.
            
            top_left = tk.Button(frame, bg=bg_color, text=table[0],
                                 command=lambda: [text_change(top_left), modify_table(0), stop_func()])
            top_center = tk.Button(frame, bg=bg_color, text=table[1],
                                   command=lambda: [text_change(top_center), modify_table(1), stop_func()])
            top_right = tk.Button(frame, bg=bg_color, text=table[2],
                                  command=lambda: [text_change(top_right), modify_table(2), stop_func()])
            mid_left = tk.Button(frame, bg=bg_color, text=table[3],
                                 command=lambda: [text_change(mid_left), modify_table(3), stop_func()])
            mid_center = tk.Button(frame, bg=bg_color, text=table[4],
                                   command=lambda: [text_change(mid_center), modify_table(4), stop_func()])
            mid_right = tk.Button(frame, bg=bg_color, text=table[5],
                                  command=lambda: [text_change(mid_right), modify_table(5), stop_func()])
            bottom_left = tk.Button(frame, bg=bg_color, text=table[6],
                                    command=lambda: [text_change(bottom_left), modify_table(6), stop_func()])
            bottom_center = tk.Button(frame, bg=bg_color, text=table[7],
                                      command=lambda: [text_change(bottom_center), modify_table(7), stop_func()])
            bottom_right = tk.Button(frame, bg=bg_color, text=table[8],
                                     command=lambda: [text_change(bottom_right), modify_table(8), stop_func()])

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
