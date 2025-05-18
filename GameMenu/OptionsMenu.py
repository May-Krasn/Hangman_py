import tkinter as tk

from shared_stuff import window, hide_window, clear_window
from GameMenu.SharedMenu import back_window
from  DataWork.words_work import get_difficulty, get_all_categories

# ======== WINDOW

def show_opt_window():
    global cat_label, cat_button, cat_name, err_label, err_button, err_amount, diff_label, diff_button, diff_id, back_button
    cat_label = tk.Label(window, text=f"Current category: {cat_name}")
    err_label = tk.Label(window, text=f"Current errors allowed: {err_amount}")
    diff_label = tk.Label(window, text=f"Current difficulty: {get_difficulty(diff_id)}")

    cat_button = tk.Button(window, text="Change category", command=lambda: change_cat())
    err_button = tk.Button(window, text="Change amount", command=lambda: change_err())
    diff_button = tk.Button(window, text="Change difficulty", command=lambda: change_diff())
    back_button = tk.Button(window, text="Back", command=lambda: back_window())

    config_widgets()
    place_opt_window()

def place_opt_window():
    cat_label.place(relx=0.5, y=90, anchor=tk.CENTER)
    cat_button.place(relx=0.5, y=145, anchor=tk.CENTER)
    err_label.place(relx=0.5, y=210, anchor=tk.CENTER)
    err_button.place(relx=0.5, y=265, anchor=tk.CENTER)
    diff_label.place(relx=0.5, y=330, anchor=tk.CENTER)
    diff_button.place(relx=0.5, y=385, anchor=tk.CENTER)
    back_button.place(relx=0.5, y=500, anchor=tk.CENTER)

# ===== BUTTONS

buttons = []
lbl = None
def change_cat():
    hide_window()
    cats = get_all_categories()

    text = tk.Text(window)
    text.pack(side=tk.LEFT, fill=tk.BOTH)

    sb = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    text.configure(yscrollcommand=sb.set)

    lbl = tk.Label(window, text="Choose a category", font=("Comic Sans MS", 20))
    text.window_create(tk.END, window=lbl)
    text.insert(tk.END, "\n")

    buttons = []
    cats.append("random")
    for cat in cats:
        btn = tk.Button(text, text=cat, command=lambda msg=cat: on_click(msg), font=("Comic Sans MS", 16))
        text.window_create(tk.END, window=btn, pady=4)
        text.insert(tk.END, "\n")
        buttons.append(btn)
    text.configure(state=tk.DISABLED)

    def on_click(msg):
        global cat_name, cat_label
        cat_name = msg
        cat_label.config(text=f"Current category: {cat_name}")
        for btn in buttons:
            btn.destroy()
        lbl.destroy()
        sb.destroy()
        text.destroy()
        place_opt_window()
        return

def change_diff():
    global buttons, lbl
    hide_window()
    lbl = tk.Label(window, text="Choose difficulty", font=("Comic Sans MS", 20))
    lbl.place(relx=0.5, y=90, anchor=tk.CENTER)
    buttons = []
    btn1 = tk.Button(window, text="Easy", command=lambda: on_click_diff(1), font=("Comic Sans MS", 16))
    btn2 = tk.Button(window, text="Medium", command=lambda: on_click_diff(2), font=("Comic Sans MS", 16))
    btn3 = tk.Button(window, text="Hard", command=lambda: on_click_diff(3), font=("Comic Sans MS", 16))
    btn4 = tk.Button(window, text="Random", command=lambda: on_click_diff(0), font=("Comic Sans MS", 16))
    buttons.append(btn1)
    buttons.append(btn2)
    buttons.append(btn3)
    buttons.append(btn4)

    btn1.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
    btn2.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
    btn3.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    btn4.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
def on_click_diff(msg):
    global diff_label, diff_id
    diff_id = msg
    diff_label.config(text=f"Current difficulty: {get_difficulty(diff_id)}")
    for btn in buttons:
        btn.destroy()
    lbl.destroy()
    place_opt_window()
    return

def change_err():
    global buttons, lbl
    hide_window()
    lbl = tk.Label(window, text="Choose amount of errors", font=("Comic Sans MS", 20))
    lbl.place(relx=0.5, y=140, anchor=tk.CENTER)
    btn1 = tk.Button(window, text="10", command=lambda: on_click_errors(10), font=("Comic Sans MS", 22))
    btn2 = tk.Button(window, text="5", command=lambda: on_click_errors(5), font=("Comic Sans MS", 22))
    btn3 = tk.Button(window, text="3", command=lambda: on_click_errors(3), font=("Comic Sans MS", 22))
    buttons.append(btn1)
    buttons.append(btn2)
    buttons.append(btn3)

    btn1.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
    btn2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    btn3.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
def on_click_errors(msg):
    global err_amount, err_label
    err_amount = msg
    err_label.config(text=f"Current errors allowed: {err_amount}")
    for btn in buttons:
        btn.destroy()
    for btn in buttons:
        buttons.remove(btn)
    lbl.destroy()
    place_opt_window()
    return

# ==== configs

def config_widgets():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(font=("Comic Sans MS", 16), bg="#E4E2E2", fg="#000")
        if isinstance(widget, tk.Label):
            widget.config(font=("Comic Sans MS", 16))
            widget.pack(expand=True)

# ====== GLOBALS
# category
cat_label = None
cat_button = None
cat_name = "random"
# errors
err_label = None
err_button = None
err_amount = 10
# difficulty
diff_label = None
diff_button = None
diff_id = 0 # 0 - random
# back button
back_button = None