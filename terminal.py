#region start
"""
The terminal version (the core)
input(), while, import quiz.py functions 
"""
#endregion

import os
import shutil
import sys
import textwrap
import time
from typing import NamedTuple
from collections.abc import Callable

import quiz
import storage


class MenuOption(NamedTuple):
    label: str
    action: Callable[[], None] # Callable is the type hint for functions

class Link(NamedTuple):
    text: str
    url: str

# is_running: bool = False
# is_running_test: bool = True

questions = storage.load_questions()
high_scores = storage.load_high_scores()

def say_hi():
    print("Hello from terminal.py")

# quiz.print_question_ids(questions)

# print("This is random choice in action")
# print(quiz.get_random_question(questions))

# storage.read_file('questions.json')

def prompt_choice(prompt, options) -> None:
    pass

def ask_question() -> dict:
    print("Ask a question called")

    return quiz.get_random_question(questions)

def quick_start() -> None:
    print("Quick start called")

def select_a_list() -> None:
    print("Select a list called")

def view_high_scores() -> None:
    print("View high scores called")

def view_questions() -> None:
    print("View questions called")


def view_credits() -> None:
    print_credits()

def run_quiz() -> None:
    print("Running quiz...\n\n\n")
    user_input = input("\nSelect an option (1-4)...").strip()

    if user_input == "done":
        print("\n\n\n.")
    else:
        print("Did not work.")

def print_question_ids(questions: list[dict]) -> None:
    """Print a list of question ids"""
    ids_list = [question['id'] for question in questions]
    print(*ids_list, sep='\n')


def show_high_scores() -> None:
    pass

def centered_url(*links: Link, sep: str =" — ") -> str:
    """Return a centered string combining multiple Link objects"""
    texts = [text for text, url in links]
    result = centered(sep.join(texts))
    for text, url in links:
        result = result.replace(text, link(text, url))
    return result

def print_credits() -> None:
    """Print a menu of credits with clickable and centered links for flair"""
    print('\n' * 5)
    print_divider()
    print('\n' * 1)

    print(centered('Created by Oswaldo Fabrizio De Los Santos Ascencio'))
    print(
        centered_url( # A single function call with multiple Link objects
            Link(text="Visit my Github", url="https://github.com/oswwwaldo"),
            Link(text="Visit the repository", url="https://github.com/oswwwaldo/professor-quack-py"), 
            Link(text="Visit my LinkedIn", url="https://linkedin.com/oswwwaldo"),
        ) 
    )

    print('\n' * 1)
    print_divider()

def print_menu(title: str, options: list[MenuOption]) -> None:
    """Print a reuseable menu using the MenuOption class"""
    print(f'\n{title}:')
    for number, option in enumerate(options, start=1):
        print(f"[{number}] — {option.label}")

def prompt_user_input(options: list[MenuOption]) -> bool:
    user_input = input(f"\nSelect an option (1 - {len(options)})...").strip()

    try:
        chosen_menu_option = options[int(user_input) - 1]
        _, func = chosen_menu_option 
    except NameError:
        print("Item does not exist in memory")
        raise
    except ValueError:
        print("Not a valid value")
        raise
    except IndexError:
        print(f"\nInvalid input — you entered {user_input}.\nPlease select an option between (1 - {len(options)})...")
        time.sleep(2.5)

    if func == None:
        return False
    else:
        chosen_menu_option.action()
        return True

options = [
    MenuOption("Quick start", quick_start),
    MenuOption("Select a list", select_a_list),
    MenuOption("View high scores", view_high_scores),
    MenuOption("View all questions", view_questions),
    MenuOption("Credits", view_credits),
    MenuOption("Return to main menu", None),
]

def main_menu() -> None:
    """A while loop with user input and menu options"""
    is_running: bool = True
    while True:
        print_menu("CLI Terminal", options)
        is_running = prompt_user_input(options)
        if not is_running:
            break


# size = shutil.get_terminal_size()
# print("The whole object:", size)
# size.columns = horizontal, size.lines = vertical

# columns, lines = size

def print_divider(char: str = "=") -> None:
    """Print a line of `char` that spans the terminal's current width via shutil"""
    width = shutil.get_terminal_size().columns
    print(char * width)

def centered(text: str, fill: str = " ") -> str:
    """Return a padded string object centered in the middle of the terminal window via shutil"""
    width = shutil.get_terminal_size().columns
    return text.center(width, fill)
    
def link(text: str, url: str, end: str = '\n') -> str:
    """Print a clickable URL to the terminal, supported by modern terminals — using the OSC 8 ANSI escape sequence"""
    return (f"\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\")