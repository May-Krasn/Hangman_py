import tkinter as tk

from DataWork.users_work import login_user
import menu.shared_menu as sm
from GameMenu.PlayerMenu import place_on_window as game_window
from shared_stuff import clear_window


#   ====== WINDOW =======

def place_on_window():
    sm.loginLabel.place(x=100, y=95)
    sm.passwordLabel.place(x=70, y=165)
    sm.loginTextField.place(x=180, y=90, width=360, height=60)
    sm.passwordTextField.place(x=180, y=160, width=360, height=60,)
    sm.inputConfirm.place(x=180, y=230, width=160, height=40)
    sm.backButton.place(x=380, y=230, width=160, height=40)

def log_window():
    sm.create_shared(lambda: take_input())
    place_on_window()


#   ==== Button Work ====

def take_input():
    inputLogin = sm.loginTextField.get("1.0", tk.END).strip()
    inputPassword = sm.passwordTextField.get().strip()

    if inputLogin == "" or inputPassword == "":
        sm.errorLabel.config(text="Please, enter a valid character")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return

    if (len(inputPassword) < 8 or not any(char.isdigit() for char in inputPassword)
            or not any(char.isalpha() for char in inputPassword)):
        sm.errorLabel.config(text="Not a valid password")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return

    response = login_user(inputLogin, inputPassword)
    if response == "wrong password":
        sm.errorLabel.config(text="Wrong password")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return
    elif response == "wrong login":
        sm.errorLabel.config(text="User doesn't exist")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return
    else:
        # ----> przejscie do gry
        clear_window()
        game_window(inputLogin, response)
        return

