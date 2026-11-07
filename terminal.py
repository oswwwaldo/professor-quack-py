#region start
"""
The terminal version (the core)
input(), while, import quiz.py functions 
"""
#endregion

import os
import shutil
import time
from collections.abc import Callable
from typing import NamedTuple

import readchar
from readchar import key

import quiz
import storage


class MenuOption(NamedTuple):
    label: str
    action: Callable[[], None] | None # Callable is the type hint for functions


Controller = Callable[[list[MenuOption], str], int] # Type-hinting for handle_keys/input_controllers

class Link(NamedTuple):
    text: str
    url: str

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
    """Run quick start mode, immediately throwing a question for the user to answer randomly"""
    # should store a history of correct and incorrect questions into another function

    while True:
        question = quiz.get_random_question(questions)

        options = [
            MenuOption(label, action)
            for label, action in question['choices'].items()
        ]

        print(f"\n{question['id']} —")
        print(f"{question['question']}")

        for letter, text in options:
            print(f"({letter}) — {text}")

        letters = [letter for letter, _ in options]
        call_controller = return_active_controller()
        user_input = call_controller(options, question['id'])

        selected_answer = letters[user_input - 1] 

        print(quiz.is_correct(question, selected_answer))
        print(quiz.get_explanation(question, selected_answer))

        options = [
            MenuOption("Next question", next_question),
            MenuOption("Return to terminal menu", None),
        ]

        print_menu("Main menu", options)
        print_divider("_")
        continue_while_loop = prompt_user_input(options)
        if not continue_while_loop:
            break

def next_question() -> None:
    """A placeholder function for the quick_start menu so 'Next question' menu option has a callable"""

def select_a_list() -> None:
    print("Select a list called")
    # all_lists = quiz.get_all_categories(questions)

    # [lst for lst in all_lists]

    # options = [
    #     MenuOption("Next question", next_question),
    #     MenuOption("Return to terminal menu", None),
    # ]

    # print_menu("Main menu", options)
    # print_divider("_")
    # continue_while_loop = prompt_user_input(options)
    # if not continue_while_loop:
    #     break

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

use_keys_controller: bool = False
use_input_controller: bool = True

def return_active_controller() -> Controller:
    if (use_keys_controller is True):
        return handle_keys_controller
    elif (use_input_controller is True):
        return handle_input_controller
    else:
        raise NameError("No controller found")

def prompt_user_input(options: list[MenuOption] | None) -> bool:
    if options is None:
        return False 

    if (use_keys_controller is True):
        user_input = handle_keys_controller(options, "Use your arrow keys to navigate:") 
    elif (use_input_controller is True):
        user_input = handle_input_controller(options)
    else:
        raise ValueError("No input controller configured")

    try:
        chosen_menu_option = options[user_input - 1]
    except NameError:
        print("Item does not exist in memory")
        raise
    except ValueError:
        print("Invalid input — Cannot typecast into int()")
    except IndexError:
        print(f"\nInvalid input — you entered {user_input}.\nPlease select an option between (1 - {len(options)})...")
        time.sleep(2.5)

    if chosen_menu_option.action is None:
        return False

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

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def handle_keys_controller(options: list[MenuOption], title: str = "" ) -> int:
    """Returns a menu option (int) via key-navigation using readchar and clear_screen"""
    selected = 0

    while True:
        clear_screen()
        print(f"{title}\n")
        for index, option in enumerate(options):
            marker = ">" if index == selected else " "
            print(f" {marker} {option.label}")

        pressed = readchar.readkey()

        if pressed == key.UP:
            selected = (selected - 1) % len(options)
        elif pressed == key.DOWN:
            selected = (selected + 1) % len(options)
        elif pressed in (key.ENTER, key.RIGHT):
            return selected + 1     

def handle_input_controller(options: list[MenuOption], title: str = "" ) -> int:
    """Returns a menu option (int) via typing directly in the terminal"""
    user_input = input(f"\nSelect an option (1 - {len(options)})... ").strip()
    return int(user_input)

def activate_keys_controller() -> None:
    """Switch to keys controller, disabling input controller"""
    global use_keys_controller
    global use_input_controller

    use_keys_controller = True
    use_input_controller = False
    print(f"The input controller is now {use_keys_controller}")
    print(f"The keys controller is now {use_input_controller}")
    print(activate_keys_controller)

def activate_input_controller() -> None:
    """Switch to input controller, disabling keys controller"""
    global use_keys_controller
    global use_input_controller

    use_keys_controller = False
    use_input_controller = True
    print(f"The input controller is now {use_keys_controller}")
    print(f"The keys controller is now {use_input_controller}")
    print(activate_input_controller)
