import tkinter as tk
from tkinter import Frame, font as tkFont, colorchooser, messagebox
import json

# Getting the default theme settings

with open('settings.json', 'r') as s:
    settings = json.load(s)

default = settings[0]["Default_theme"]

def start(color: int):

    # Function to start the game.
    # Takes 1 argument, 'color': Theme of the game.

    # Game window initiation

    root = tk.Tk()
    root.geometry("600x600")
    root.resizable(False, False)

    # Theme assignment

    with open('themes.json', 'r') as f:
        theme = json.load(f)

    num_of_themes = len(theme)
    bg_color = theme[color]["bg_color"]
    frame_color = theme[color]["frame_color"]
    fg_color = theme[color]["fg_color"]

    def endgame_widget(result):

        # Function to show the widget at the end of each game.
        # Takes 1 argument, 'result': Result of the game.
        # Shows the result and has 2 buttons; 'Restart' and 'Quit'.

        # Endgame widget initiation

        widget = tk.Tk()
        widget.geometry("300x100")
        widget.resizable(False, False)

        if result == "Tie":
            res_text = "It is a tie!"
        else:
            res_text = result + " is the winner!"

        frame = tk.LabelFrame(widget, bg=frame_color,
                              fg=fg_color, text=res_text, labelanchor="n")
        frame.place(relheight=1, relwidth=1)

        restart = tk.Button(frame, bg=bg_color, fg=fg_color, text="Restart",
                            command=lambda: [widget.destroy(), game()])
        restart.pack()

        qt = tk.Button(frame, bg=bg_color, fg=fg_color, text="Quit",
                       command=lambda: [widget.destroy(), root.destroy()])
        qt.pack()

        widget.mainloop()

    def game():

        # Main function to run the game.
        # Game logic and GUI are both in this function.

        # Table array keeps what each cell holds.
        # Necessary for the game logic.

        table = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]

        default_font = tkFont.Font(family="Helvetica", size=50, weight="bold")

        def menubar_creation():

            # Function to create a menubar.

            def theme_selection():
                
                # Function to create a theme change widget.

                def choose_theme(num):
                    
                    # Function to change the theme.
                    # Takes 1 argument, 'num': Newly selected theme number.
                    
                    with open('settings.json', 'r+') as s:
                        settings = json.load(s)
                        settings.append({"Default_theme": num})
                        settings.pop(0)
                    with open('settings.json', 'w') as s:
                        settings = json.dump(settings, s, indent=4)   

                    selector.destroy()
                    root.destroy()
                    start(num)
                    
                    
                def create_new_theme():
                    
                    # Function to create a new theme.
                    # Uses the add_to_json function to append the newly created theme to the json file.
                    # Uses the colorchooser of tkinter library.
                    
                    def add_to_json(new_data):
                        
                        with open('themes.json', 'r+') as f:
                            theme = json.load(f)
                            theme.append(new_data)
                            f.seek(0)
                            json.dump(theme, f, indent=4)
                            
                    # Color picking for the new theme
                    
                    new_bg = colorchooser.askcolor(title="Background color")[1]
                    new_fg = colorchooser.askcolor(title="Foreground color")[1]
                    new_frame = colorchooser.askcolor(title="Frame color")[1]
                    
                    new_thm = {
                        "bg_color" : new_bg,
                        "frame_color" : new_frame,
                        "fg_color" : new_fg
                    }
                    
                    add_to_json(new_thm)
                
                
                def check_deletable():
                    
                    # Fucntion to check if there are any deletable themes.
                    # A deletable theme is one that has been previously created 
                    #                          by the use and not a default one.
                    # If there are any deletable themes, delete theme widget opens.
                    # If not, the user is alerted that there are no deletable themes.
                    
                    num_of_def_themes = 3
                    
                    if num_of_themes > num_of_def_themes:
                        delete_theme_widget()
                    else:
                        messagebox.showinfo("No Deletable Themes", "There are only default themes. You can only delete user created themes.")
                
                
                def delete_theme_widget():
                    
                    def delete_theme(num):
                        
                        # Function to delete the chosen theme.
                        # Takes 1 argument, 'num': Number of the theme to be deleted
                        
                        with open('themes.json', 'r') as f:
                            theme = json.load(f)
                            theme.pop(num)
                        with open('themes.json', 'w') as f:
                            theme = json.dump(theme, f)                       
                            
                    # Function to create a delete theme widget.
                    # Deleting the, currently 3, default themes is not possible.
                    
                    num_of_def_themes = 3
                    dw_height = height-100 * num_of_def_themes
                    
                    del_widget = tk.Tk()
                    del_widget.maxsize(width, dw_height)
                    del_widget.minsize(width, dw_height)
                    del_widget.resizable(False, False)
                    
                    dw_frame = tk.Frame(del_widget, bg=frame_color)
                    dw_frame.place(relheight=1, relwidth=1)

                    dw_theme_buttons = []
                    dw_theme_num = 0

                    # Creating theme buttons to choose from.

                    for thm in theme:
                        if dw_theme_num < num_of_def_themes:
                            dw_theme_num += 1
                        else:
                            button_text = "Theme " + str(dw_theme_num + 1)
                            new_button = tk.Button(
                                dw_frame, bg=thm["bg_color"], fg=thm["fg_color"], text=button_text)
                            dw_theme_buttons.append(new_button)
                            dw_theme_buttons[dw_theme_num-num_of_def_themes].config(font=default_font)
                            dw_theme_buttons[dw_theme_num-num_of_def_themes].place(
                                x=0, y=100*(dw_theme_num-num_of_def_themes), height=100, width=300)
                            dw_theme_num += 1

                    for i in range(0, len(dw_theme_buttons)):
                        dw_theme_buttons[i]["command"] = lambda i=i: [delete_theme(i+num_of_def_themes), del_widget.destroy(), root.destroy(), start(default)]
                                        
                # Theme selection widget initiation

                width = 300
                height = num_of_themes * 100

                selector = tk.Tk()
                selector.maxsize(width, height)
                selector.minsize(width, height)
                selector.resizable(False, False)
                
                # Create new theme menu
                
                create = tk.Menu(selector, bg=bg_color, fg=fg_color)
                new_theme = tk.Menu(create, tearoff=0)
                new_theme.add_command(label="New Theme", command=lambda: [selector.destroy(), create_new_theme()])
                new_theme.add_command(label="Delete Theme", command=lambda: [selector.destroy(), check_deletable()])
                create.add_cascade(label="Options", menu=dropdown)
                
                selector.config(menu=create)

                theme_frame = tk.Frame(selector, bg=frame_color)
                theme_frame.place(relheight=1, relwidth=1)

                theme_buttons = []
                theme_num = 0

                # Creating theme buttons to choose from.

                for thm in theme:
                    button_text = "Theme " + str(theme_num + 1)
                    new_button = tk.Button(
                        theme_frame, bg=thm["bg_color"], fg=thm["fg_color"], text=button_text)
                    theme_buttons.append(new_button)
                    theme_buttons[theme_num].config(font=default_font)
                    theme_buttons[theme_num].place(
                        x=0, y=100*theme_num, height=100, width=300)
                    theme_num += 1

                for i in range(0, len(theme_buttons)):
                    theme_buttons[i]["command"] = lambda i=i: choose_theme(i)

            menubar = tk.Menu(root, bg=bg_color, fg=fg_color)
            dropdown = tk.Menu(menubar, tearoff=0)
            dropdown.add_command(label="Theme", command=lambda: [
                                 theme_selection()])
            dropdown.add_command(label="Restart", command=lambda: [
                                 root.destroy(), start(default)])
            dropdown.add_command(label="Quit", command=root.destroy)
            menubar.add_cascade(label="Menu", menu=dropdown)

            root.config(menu=menubar)

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
            # Returns 'X' or 'O' or 'None'.

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
                endgame_widget(winner)
            elif check_full_table():
                print("There is a tie!")
                endgame_widget("Tie")

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
            # Takes 1 argument, 'num': Position of the move on the table.
            # Uses count_moves() to determine the turn.

            if count_moves() % 2:
                table[num] = "O"
            else:
                table[num] = "X"
            print(table)

        def text_change(bttn: tk.Button):

            # Function to implement the necessary adjustments on the last played cell based on the last move.
            # Takes 1 argument, 'bttn': The button that has been clicked.

            if count_moves() % 2:
                bttn.configure(text="O")
            else:
                bttn.configure(text="X")

        def click(bttn: tk.Button, num: int):

            # Function to make a move when a button is clicked, if it is legal.
            # Takes 2 arguments, 'bttn': The button that has been clicked.
            #                    'num': Position of the move on the table.
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

            for btn in buttons:
                btn.config(font=default_font)
                btn.configure(fg=fg_color)

            # Cell placement

            a = 0.01
            top_left.place(relx=2 * a, rely=2 * a,
                           relwidth=30 * a, relheight=30 * a)
            top_center.place(relx=35 * a, rely=2 * a,
                             relwidth=30 * a, relheight=30 * a)
            top_right.place(relx=68 * a, rely=2 * a,
                            relwidth=30 * a, relheight=30 * a)
            mid_left.place(relx=2 * a, rely=35 * a,
                           relwidth=30 * a, relheight=30 * a)
            mid_center.place(relx=35 * a, rely=35 * a,
                             relwidth=30 * a, relheight=30 * a)
            mid_right.place(relx=68 * a, rely=35 * a,
                            relwidth=30 * a, relheight=30 * a)
            bottom_left.place(relx=2 * a, rely=68 * a,
                              relwidth=30 * a, relheight=30 * a)
            bottom_center.place(relx=35 * a, rely=68 * a,
                                relwidth=30 * a, relheight=30 * a)
            bottom_right.place(relx=68 * a, rely=68 * a,
                               relwidth=30 * a, relheight=30 * a)

        frame = tk.Frame(root, bg=frame_color)
        frame.place(relwidth=1, relheight=1)

        button_creation()
        menubar_creation()

    game()
    root.mainloop()


start(default)
