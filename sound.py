import os

# from terminal import MenuOption

if os.name == "nt":
    import winsound

# TODO: Import boss music, combat, intro, notification, faaha, levle-up, quest_update and skill-up

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