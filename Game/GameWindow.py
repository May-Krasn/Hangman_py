import tkinter as tk
from shared_stuff import window, clear_window
from string import ascii_lowercase
from DataWork.words_work import get_word, get_word_random
import time


def start_game(category, difficulty, errors_got):
    global start_time, errors_change
    errors_change = errors_got
    place_canva()
    place_keyboard()
    place_word(category, difficulty)
    start_time = time.time()

# ====== GAME

def hangman():
    global errors, canvas

    # depending on amount of errors choosen by player
    # we're adding errors and making drawing

    if errors_change == 10: n = 1
    elif errors_change == 5:n = 2
    else:
        if errors == 0: n = 4
        else: n = 3

    for i in range(n):
        errors += 1
        match errors:
            case 1:
                canvas.create_line(20, 200, 170, 200, width=5)
            case 2:
                canvas.create_line(55, 200, 55, 30, width=5)
                canvas.create_line(40, 200, 55, 185, width=5)
                canvas.create_line(70, 200, 55, 185, width=5)
            case 3:
                canvas.create_line(55, 30, 145, 30, width=5)
                canvas.create_line(55, 45, 75, 30, width=5)
            case 4:
                canvas.create_line(130, 30, 130, 60, width=5)
            case 5:
                canvas.create_oval(115, 60, 145, 90, width=5)
            case 6:
                canvas.create_line(130, 90, 130, 140, width=5)
            case 7:
                canvas.create_line(130, 100, 115, 120, width=5)
            case 8:
                canvas.create_line(130, 100, 145, 120, width=5)
            case 9:
                canvas.create_line(130, 139, 115, 165, width=5)
            case 10:
                canvas.create_line(130, 140, 145, 165, width=5)
                lbl = tk.Label(window, text="GAME OVER", font=("Comic Sans MS", 24), bg="#B56E6D", fg="white")
                lbl.place(x=20, y=20, width=385, height=150)
                index = 0
                while index < len(word):
                    letters[index].config(text=word[index])
                    index += 1
                for widget in window.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(state=tk.DISABLED)
                window.after(3000, lambda: game_over(False))

def game_over(won):
    global errors, corrects, letters, word
    errors, corrects = 0, 0
    letters.clear()
    word = ""
    from GameMenu.PlayerMenu import place_on_window, login, name
    clear_window()

    end_time = time.time() - start_time
    mins = int(end_time) // 60
    secs = int(end_time) % 60

    if login != "Guest":
        from DataWork.users_work import update_stats
        if won:
            update_stats(login, 1, 1, mins, secs)
        else:
            update_stats(login, 1, 0, mins, secs)

    place_on_window(login, name)

# ========= WORD

def place_word(cat, diff):
    global letters, word
    if cat == "random" and diff == 0:
        cat, word = get_word_random()
    else:
        word = get_word(cat, diff)
    lbl = tk.Label(window, text=f"Category:\n{cat}", font=("Comic Sans MS", 24))
    lbl.pack(expand=True)
    lbl.place(relx=0.3, y=100, anchor=tk.CENTER)

    letter_frame = tk.Frame(window, bg="#E4E2E2")
    letter_frame.pack(expand=True)
    letter_frame.place(relx=0.5, y=315, height=50, anchor=tk.CENTER)

    for letter in word:
        lbl = tk.Label(letter_frame, text="_", font=("Comic Sans MS", 16), bg="#E4E2E2")
        if letter == " ":
            lbl.config(text=" ")
        lbl.pack(side=tk.LEFT, padx=5)
        letters.append(lbl)

# ========= KEYBOARD

def place_keyboard():
    global buttons

    for char in ascii_lowercase:
        buttons[char] = tk.Button(window, text=char, command=lambda c=char: on_click(c), font=("Comic Sans MS", 16), disabledforeground="white")

    for i in range(len(buttons)):
        if i < 20: buttons.get(ascii_lowercase[i]).place(x=35+(60*(i%10)), y=350+(75*int((i/10))), width=50, height=50)
        else: buttons.get(ascii_lowercase[i]).place(x=155+(60*(i%10)), y=500, width=50, height=50)

def on_click(x):
    global corrects

    if not word.__contains__(x):
        buttons.get(x).config(state=tk.DISABLED, bg='gray')
        hangman()
    else:
        buttons.get(x).config(state=tk.DISABLED, bg='lightgreen')
        index=0
        while index < len(word):
            index = word.find(x, index)
            if index == -1: break
            letters[index].config(text=x)
            index +=1
            corrects += 1

        if corrects == len(word.replace(" ", "")):
            lbl = tk.Label(window, text="YOU WON", font=("Comic Sans MS", 24), bg="#85B987", fg="white")
            lbl.place(x=20, y=20, width=385, height=150)
            for widget in window.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(state=tk.DISABLED)
            window.after(3000, lambda: game_over(True))

# ========= CANVA

def place_canva():
    global canvas
    canvas = tk.Canvas(master=window, width=200, height=250)
    canvas.place(x=430, y=10)

# ========= GLOBALS
buttons = {}
errors = 0
corrects = 0
errors_change = 10
canvas = None
letters = []
word = ""
start_time = None