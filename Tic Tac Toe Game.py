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
    
    frame = tk.Frame(root, bg=frame_color)
    frame.place(relwidth=1, relheight=1)
    
    root.mainloop()
    
start()
