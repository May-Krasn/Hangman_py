import tkinter as tk

from src.DataWork.users_work import add_user
from src.menu.shared_stuff import window
import src.menu.shared_menu as sm

#  ==== CREATE ====

def create_for_reg():
    """
    widgets for Register window
    """
    global nameLabel, nameTextField
    nameLabel = tk.Label(master=window, text="Name:")
    nameLabel.config(font=("Comic Sans MS", 16), bg="#E4E2E2")

    nameTextField = tk.Text(master=window, bg="#E4E2E2", font=("Comic Sans MS", 16))
    nameTextField.bind("<KeyPress>", sm.on_key_press)

def place_on_window():
    """
    Places widgets on window
    """
    sm.loginLabel.place(x=100, y=95)
    nameLabel.place(x=100, y=165)
    sm.passwordLabel.place(x=70, y=235)
    sm.loginTextField.place(x=180, y=90, width=360, height=60)
    nameTextField.place(x=180, y=160, width=360, height=60)
    sm.passwordTextField.place(x=180, y=230, width=360, height=60)
    sm.inputConfirm.place(x=180, y=300, width=160, height=40)
    sm.backButton.place(x=380, y=300, width=160, height=40)

def reg_window():
    """
    function called from other class to create window for Registration
    """
    sm.create_shared(lambda: take_input())
    create_for_reg()
    place_on_window()


#   ==== Button Work ====

def take_input():
    """
    Info validation for Confirm button
    :return: error or success label on window
    """
    inputLogin = sm.loginTextField.get("1.0", tk.END).strip()
    inputName = nameTextField.get("1.0", tk.END).strip()
    inputPassword = sm.passwordTextField.get().strip()

    if inputLogin == "" or inputPassword == "" or inputName == "":
        sm.errorLabel.config(text="Please, enter a valid character")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return

    if (len(inputPassword) < 8 or not any(char.isdigit() for char in inputPassword)
            or not any(char.isalpha() for char in inputPassword)):
        sm.errorLabel.config(text="Please, enter a valid password\n8+ characters\nat least one digit and one letter")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return

    response = add_user(inputLogin, inputName, inputPassword)
    if response != "success":
        sm.errorLabel.config(text="Login already exists")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return
    else:
        sm.errorLabel.config(text="User created")
        sm.errorLabel.place(x=140, y=380, width=400, height=100)
        return

# ==== globals ====

nameLabel = None
nameTextField = None