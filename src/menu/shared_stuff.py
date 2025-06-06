import tkinter as tk

window = tk.Tk()
window.config(bg="#cbcbcb")
window.title("Hangman")
window.geometry("690x570")
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", exit)

def clear_window():
    """
    fully destroys widgets on window to clear it
    """
    for widget in window.winfo_children():
        widget.destroy()

def hide_window():
    """
    Uses '.place_forget()' to hide the window in case we need to return to it
    :return:
    """
    for widget in window.winfo_children():
        widget.place_forget()

def config_buttons():
    """
    configures every created button to game style
    """
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(bg="#E4E2E2", fg="#000", font=("Comic Sans MS", 16))
