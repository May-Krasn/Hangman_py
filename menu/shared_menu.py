import tkinter as tk
from string import ascii_letters, punctuation, digits

from shared_stuff import window, clear_window, config_buttons

# ==== WINDOW ====

def create_shared(fun : callable):
    global loginLabel, passwordLabel, loginTextField, passwordTextField, inputConfirm, backButton, errorLabel
    loginLabel = tk.Label(master=window, text="Login:")
    loginLabel.config(font=("Comic Sans MS", 16), bg="#E4E2E2")
    passwordLabel = tk.Label(master=window, text="Password:")
    passwordLabel.config(font=("Comic Sans MS", 16), bg="#E4E2E2")

    loginTextField = tk.Text(master=window, bg="#E4E2E2", font=("Comic Sans MS", 16))
    loginTextField.bind("<KeyPress>", on_key_press)

    passwordTextField = tk.Entry(master=window, bg="#E4E2E2", font=("Comic Sans MS", 16), show='*')
    passwordTextField.bind("<KeyPress>", on_key_press)

    errorLabel = tk.Label(master=window)
    errorLabel.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))

    inputConfirm = tk.Button(master=window, text="Confirm", command=fun)
    backButton = tk.Button(master=window, text="Back", command=lambda: back_window())

    config_buttons()

#   ==== Button Work ====

def back_window():
    clear_window()
    from menu.MainMenu import place_on_window as mainplace
    mainplace()

# ==== Info valid ====

def on_key_press(event):
    if event.keysym == "BackSpace":
        widget = event.widget
        if isinstance(widget, tk.Entry):
            widget.delete(len(widget.get()), tk.END)
        else:
            widget.delete("end-1c", tk.END)
        return

    if event.keysym in ("Left", "Right", "Delete"):
        return "break"

    char = event.char
    if char not in (ascii_letters + punctuation + digits) and char :
        return "break"

    if isinstance(event.widget, tk.Entry):
        if len(event.widget.get()) == 30:
            return "break"
        return

    if len(event.widget.get("1.0", tk.END)) == 30:
        return "break"

# ==== globals ====

loginLabel = None
passwordLabel = None

loginTextField = None
passwordTextField = None

inputConfirm = None
backButton = None

errorLabel = None