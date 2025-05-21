import tkinter as tk
from PIL import Image, ImageTk

from src.menu.shared_stuff import window, clear_window, hide_window, config_buttons
from src.menu.RegisterUser import reg_window
from src.menu.LoginUser import log_window
from src.GameMenu.PlayerMenu import place_on_window as game_window

#   ====== USER =======

def register_user():
    """
    To go to Registration window
    """
    clear_window()
    reg_window()

def login_user():
    """
    To go to Login window
    """
    clear_window()
    log_window()

#   ====== GUEST GAME =======

def start_guest():
    """
    Starting game as guest
    Contains buttons to confirm or go back to main window
    """
    hide_window()
    def resign():
        confirmation.destroy()
        resignation.destroy()
        askinglabel.destroy()
        place_on_window()
    def confirm():
        confirmation.destroy()
        resignation.destroy()
        askinglabel.destroy()
        clear_window()
        # ----> przejscie do gry
        game_window("Guest", "Guest")


    askinglabel = tk.Label(master=window, text="Are you sure?\nYour data won't be saved", font=("Comic Sans MS", 16))
    askinglabel.config(bg="#E4E2E2", fg="#000")
    askinglabel.place(x=140, y=200, width=400, height=80)

    confirmation = tk.Button(master=window, text="Yes :0", command=lambda: confirm())
    confirmation.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))
    resignation = tk.Button(master=window, text="Oh, no!", command=lambda: resign())
    resignation.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))
    confirmation.place(x=140, y=300, width=150, height=40)
    resignation.place(x=380, y=300, width=150, height=40)

#   ====== CREATE WINDOW =======
# Plus clearing exported stats

def main():
    """
    Main function
    """
    exported_clear()
    place_on_window()
    window.mainloop()

def exported_clear():
    """
    checks exported directory. Clears it if there is anything in it
    creates directory if it's not created
    :return:
    """
    import os
    try:
        if os.listdir("Exported"):
            for file in os.listdir("Exported"):
                os.remove(os.path.join("Exported", file))
    except FileNotFoundError:
        os.mkdir("Exported")


#   ====== WINDOW =======

def create_for_window():
    """
    Creates widgets
    """
    global startguest, loginuser, registeruser, canvas, madeby, image, exitbutton

    startguest = tk.Button(master=window, text="Start as Guest", command=lambda: start_guest())
    loginuser = tk.Button(master=window, text="Login", command=lambda: login_user())
    registeruser = tk.Button(master=window, text="Register", command=lambda: register_user())
    exitbutton = tk.Button(master=window, text="Exit", command=lambda: exit())

    config_buttons()

    image = ImageTk.PhotoImage(Image.open("images/HangImage.png"))
    canvas = tk.Canvas(master=window, width=206, height=257)
    canvas.create_image(0, 0, image=image, anchor=tk.NW)

    madeby = tk.Label(master=window, text="Maryia Krasnitskaya s30355")
    madeby.config(bg="#E4E2E2", fg="#000")





def place_on_window():
    """
    Places widgets on window
    """
    create_for_window()
    startguest.place(relx=0.5, y=160, width=160, height=40, anchor=tk.CENTER)
    loginuser.place(relx=0.5, y=260, width=160, height=40, anchor=tk.CENTER)
    registeruser.place(relx=0.5, y=360, width=160, height=40, anchor=tk.CENTER)
    exitbutton.place(relx=0.5, y=460, width=160, height=40, anchor=tk.CENTER)
    canvas.place(x=15, y=15)
    madeby.place(x=470, y=500, width=200, height=40)