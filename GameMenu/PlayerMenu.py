import tkinter as tk
from PIL import ImageTk, Image

from shared_stuff import window, config_buttons, clear_window, hide_window

#   ====== WINDOW =======

def create_for_window(player_login, player_name):
    global login, name
    login = player_login
    name = player_name

    global play_button, stats_button, options_button, logout_button, exit_button, canvas, madeby, image, welcome_label
    welcome_label = tk.Label(master=window, text=f"Welcome, {player_name}!")
    welcome_label.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 20))

    image = ImageTk.PhotoImage(Image.open("images/HangImage.png"))
    canvas = tk.Canvas(master=window, width=206, height=257)
    canvas.create_image(0, 0, image=image, anchor=tk.NW)

    madeby = tk.Label(master=window, text="Maryia Krasnitskaya s30355")
    madeby.config(bg="#E4E2E2", fg="#000")

    play_button = tk.Button(master=window, text="Play", command=lambda: play_start())
    stats_button = tk.Button(master=window, text="Stats", command=lambda: show_stats())
    options_button = tk.Button(master=window, text="Options", command=lambda: options_menu())
    logout_button = tk.Button(master=window, text="Log out", command=lambda: logging_out())
    exit_button = tk.Button(master=window, text="Exit", command=lambda: exit())

    config_buttons()
    if player_name == "Guest":
        stats_button.config(state=tk.DISABLED, disabledforeground="darkgrey")



def place_on_window(player_login, player_name):
    create_for_window(player_login, player_name)
    welcome_label.pack(expand=True)
    welcome_label.place(relx=0.5, y=50, anchor=tk.CENTER)
    play_button.place(relx=0.5, y=140, width=160, height=40, anchor=tk.CENTER)
    stats_button.place(relx=0.5, y=230, width=160, height=40, anchor=tk.CENTER)
    options_button.place(relx=0.5, y=320, width=160, height=40, anchor=tk.CENTER)
    logout_button.place(relx=0.5, y=410, width=160, height=40, anchor=tk.CENTER)
    exit_button.place(relx=0.5, y=500, width=160, height=40, anchor=tk.CENTER)
    canvas.place(x=15, y=150)
    madeby.place(x=470, y=500, width=200, height=40)

# ===== BUTTON WORK =======

def play_start():
    clear_window()
    from Game.GameWindow import start_game
    from GameMenu.OptionsMenu import cat_name, diff_id, err_amount
    start_game(cat_name, diff_id, err_amount)

def show_stats():
    hide_window()
    from GameMenu.StatsMenu import show_stats_window
    show_stats_window(login, name)

def options_fun():
    hide_window()

def logging_out():
    clear_window()
    from menu.MainMenu import place_on_window as mainplace
    mainplace()

def options_menu():
    clear_window()
    from GameMenu.OptionsMenu import show_opt_window
    show_opt_window()


# ----> globals
#buttons
play_button = None
stats_button = None
options_button = None
logout_button = None
exit_button = None
# cosmetics
welcome_label = None
madeby = None
canvas = None
image = None
# info
login = None
name = None