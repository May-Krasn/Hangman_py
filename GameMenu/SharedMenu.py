from shared_stuff import clear_window

def back_window():
    clear_window()
    from GameMenu.PlayerMenu import place_on_window, login, name
    place_on_window(login, name)