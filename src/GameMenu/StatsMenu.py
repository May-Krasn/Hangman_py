import tkinter as tk
from PIL import Image, ImageTk

from src.menu.shared_stuff import window
from src.DataWork.users_work import get_stats
from src.GameMenu.SharedMenu import back_window

# ICONS
icon_games_total = None
icon_games_won = None
icon_time_play = None
# Info
g_total, g_won, time_played = None, None, None
# Label
export_label = None

def show_stats_window(player_login, player_name):
    """
    Creates widgets
    :param player_login: str
    :param player_name: str
    """
    global icon_games_total, icon_games_won, icon_time_play, g_total, g_won, time_played
    g_total, g_won, time_played = get_stats(player_login)

    icon_games_total = ImageTk.PhotoImage(Image.open("images/game_icon.png"))
    icon_games_won = ImageTk.PhotoImage(Image.open("images/crown_icon.png"))
    icon_time_play = ImageTk.PhotoImage(Image.open("images/time_icon.png"))

    games_total = tk.Label(window, text=f"Games Total: {g_total}", image=icon_games_total, compound=tk.LEFT, font=("Comic Sans MS", 16))
    games_won = tk.Label(window, text=f"Games Won: {g_won}", image=icon_games_won, compound=tk.LEFT, font=("Comic Sans MS", 16))
    time_play = tk.Label(window, text=f"Time Playing: {time_played}", image=icon_time_play, compound=tk.LEFT, font=("Comic Sans MS", 16))

    label_name = tk.Label(window, text=f"{player_name}'s statistics", font=("Comic Sans MS", 20))
    label_name.pack(expand=True)
    label_name.place(relx=0.5, y=50, anchor=tk.CENTER)

    games_total.pack(expand=True)
    games_won.pack(expand=True)
    time_play.pack(expand=True)

    games_total.place(relx=0.5, y=150, anchor=tk.CENTER)
    games_won.place(relx=0.5, y=250, anchor=tk.CENTER)
    time_play.place(relx=0.5, y=350, anchor=tk.CENTER)


    export_button = tk.Button(master=window, text="Export", command=lambda: export(player_name))
    export_button.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))
    export_button.place(relx=0.5, y=420, anchor=tk.CENTER)

    back_button = tk.Button(master=window, text="Back", command=lambda: back_window())
    back_button.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))
    back_button.place(relx=0.5, y=480, anchor=tk.CENTER)

def export(player_name):
    """
    Exports statistics
    :param player_name: str
    :return: creates file in "Exported" folder
    """
    global export_label
    try:
        open(f"Exported/{player_name}_stats", "x")
    except FileExistsError:
        pass

    f = open(f"Exported/{player_name}_stats", 'w')
    f.write(f"{player_name}_stats\n\n")
    f.write(f"Games Total: {g_total}\n")
    f.write(f"Games Won: {g_won}\n")
    f.write(f"Time Playing: {time_played}\n")
    f.close()

    export_label = tk.Label(window, text="Exported stats, please look\nfor a file in ./Hangman/Exported\n\nPlease, remember that file will\nbe deleted after running app second time")
    export_label.config(bg="#E4E2E2")
    export_label.pack(expand=True)
    export_label.place(relx=0.75, y=450, anchor=tk.CENTER)