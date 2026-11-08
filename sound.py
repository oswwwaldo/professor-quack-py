import os

# from terminal import MenuOption

if os.name == "nt":
    import winsound
else:
    winsound = None


def play_correct() -> None:
    """A short ding for a correct answer"""
    if winsound:
        winsound.Beep(880, 100)
    else:
        print("\a", end="", flush=True)


def play_wrong() -> None:
    """A low buzz for a wrong answer"""
    if winsound:
        winsound.Beep(220, 300)
    else:
        print("\a", end="", flush=True)

def play_death() -> None:
    """Unique death sound effect for death match"""
    if winsound:
        winsound.Beep(220, 300)
    else:
        print("\a", end="", flush=True)

def toggle_sfx() -> None:
    print("Hi sfx from sound.py")

def toggle_music() -> None:
    print("Hi music from sound.py")

# def warn_windows_only_support() -> None:
#     options = [
#         MenuOption("Proceed — I use Windows", toggle),
#         MenuOption("Return to main menu", None),
#     ]
#     while True:
#         is_running = prompt_user_input(options, "This feature is supported by Windows only")
#         if not is_running:
#             break

# def toggle_music() -> None:
#     import winsound

#     options = [
#         MenuOption("Set your profile's name", enable_background_music),
#         MenuOption("Enable background music", enable_background_music),
#         MenuOption("Return to main menu", None),
#     ]
#     while True:
#         is_running = prompt_user_input(options, "CLI Terminal Settings")
#         if not is_running:
#             break