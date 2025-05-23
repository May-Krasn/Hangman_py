from src.menu.shared_stuff import clear_window


def back_window():
    """
    fun for back button
    """
    clear_window()
    from src.GameMenu.PlayerMenu import place_on_window, login, name

    place_on_window(login, name)
