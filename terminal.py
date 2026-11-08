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
    """Used to build mennus, pairs a label and an action for returning a function to call"""
    label: str
    action: Callable[[], object] | None 
    # Callable is the type hint for functions, we declare an object with a callable function that will return an object (str, None, int etc) or be an empty field

Controller = Callable[[list[MenuOption], str], int] 
# Type-hinting for handle_keys/input_controllers

class Link(NamedTuple):
    """Used to print clickable links in the terminal, pairs a text and a url"""
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

def start() -> None:
    """Opens a menu with different game modes"""
    options = [
        MenuOption("Quick start", quick_start), # easiest way to get started
        MenuOption("Arcade", arcade), # allows you to pick which questions
        MenuOption("Death match", death_match), # only one life, this is eligible for high scores
    ]

    while True:
        is_running = prompt_user_input(options, "START")
        if not is_running:
            break

#region game modes
#all game modes should store a history of correct and incorrect questions into another function
#should return a score
def quick_start() -> None:
    """Run quick start mode, immediately throwing a question for the user to answer randomly"""

    while True:
        question = quiz.get_random_question(questions)

        letters = list(question['choices'].keys())
        options = [
            MenuOption(label, None)
            for label in question['choices'].values()
        ]

        call_controller = return_active_controller()
        user_input = call_controller(options, f"{question['id']} — {question['question']}")

        selected_answer = letters[user_input - 1] 

        # Explore ways to separate the "quiz" and the "reprompt" section, this should be split since this function does too much
        # It is difficult for me to separate these two at the time of writing this because the while loop structure determines everything pretty much
        if quiz.is_correct(question, selected_answer):
            result = "Correct!"
        else:
            result = f"Not quite, the correct answer is {quiz.get_correct_letter(question)}"
        explanation = quiz.get_explanation(question, selected_answer)

        options = [
            MenuOption("Next question", next_question),
            MenuOption("Return to terminal menu", None),
        ]

        continue_while_loop = prompt_user_input(options, f"{result}\n{explanation}")
        if not continue_while_loop:
            break

def arcade() -> None:
    """Allows the user to select which questions they'd like to go"""
    while True:

        # TODO: Make it possible for a user to not have to choose a category or difficulty in the first place
        # TODO: Arcade should be infinite questions until the user stops, quick start should be a limited run of questions
        # TODO: Create a filter question
        # TODO: Note that prompt_a_difficulty may not return options sorted in this manner (easy -> med -> hard) but could be (easy -> hard -> med)

        chosen_category = prompt_a_category()
        chosen_difficulty = prompt_a_difficulty()
        available_questions = quiz.filter_questions(questions, chosen_difficulty, chosen_category)

        if len(available_questions) < 1:
            print("That is so specific! No questions could be found under those qualifiers, please try again.")
            continue

        # TODO: Implement session memory so that a player doesn't answer questions they already came across
        session_questions = available_questions.copy()
        question = quiz.get_random_question(session_questions)

        print(available_questions)

        letters = list(question['choices'].keys())
        options = [
            MenuOption(label, None)
            for label in question['choices'].values()
        ]

        call_controller = return_active_controller()
        user_input = call_controller(options, f"{question['id']} — {question['question']}")

        selected_answer = letters[user_input - 1] 

        if quiz.is_correct(question, selected_answer):
            result = "Correct!"
        else:
            result = f"Not quite, the correct answer is {quiz.get_correct_letter(question)}"
        explanation = quiz.get_explanation(question, selected_answer)

        options = [
            MenuOption("Next question", next_question),
            MenuOption("Return to terminal menu", None),
        ]

        continue_while_loop = prompt_user_input(options, f"{result}\n{explanation}")
        if not continue_while_loop:
            break

def death_match() -> None:
    """One life, timed intensive mode—this is eligible for writing to high scores"""
#endregion


def next_question() -> None:
    """A placeholder function for the quick_start menu so 'Next question' menu option has a callable"""

def prompt_a_category() -> str:
    all_categories = quiz.get_all_categories(questions)

    options = [
        MenuOption(label, None)
        for label in all_categories
    ]

    call_controller = return_active_controller()
    user_input = call_controller(options, "Select a category of questions to practice on")
    selected_category = options[user_input - 1]
    print(f"You selected: {selected_category.label}")

    return selected_category.label

def prompt_a_difficulty() -> str:
    all_difficulty_modes = quiz.get_all_difficulty_modes(questions)

    options = [
        MenuOption(label, None)
        for label in all_difficulty_modes
    ]

    call_controller = return_active_controller()
    user_input = call_controller(options, "Select your difficulty to practice on")
    selected_difficulty_mode = options[user_input - 1]
    print(f"You selected: {selected_difficulty_mode.label}")

    return selected_difficulty_mode.label

def view_high_scores() -> None:
    print("View high scores called")

def view_all_questions() -> None:
    print("View questions called")

def view_settings() -> None:
    pass

def view_credits() -> None:
    print_credits()

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
    print_divider("_")

use_keys_controller: bool = False
use_input_controller: bool = True

def return_active_controller() -> Callable:
    """Returns the function handling the controller that is in use"""
    if (use_keys_controller is True):
        return handle_keys_controller
    elif (use_input_controller is True):
        return handle_input_controller
    else:
        raise NameError("No controller found in use")

def prompt_user_input(options: list[MenuOption], title: str = "") -> bool:
    """Let the user pick an option with the active controller and run it. Returns False when the option means 'leave'"""
    call_controller = return_active_controller()
    user_input = call_controller(options, title)
    chosen_menu_option = options[user_input - 1]

    if chosen_menu_option.action is None:
        return False

    chosen_menu_option.action()
    return True

#region print functions
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
#endregion

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

def handle_input_controller(options: list[MenuOption], title: str = "") -> int:
    """Returns a menu option (int) via typed input in the terminal"""
    print_menu(title, options)

    while True:
        user_input = input(f"\nSelect an option (1 - {len(options)})... ").strip()

        if not user_input.isdigit():
            print(f"Please enter a number from 1 to {len(options)}.")
            continue

        choice = int(user_input)
        if not 1 <= choice <= len(options):
            print(f"Please enter a number from 1 to {len(options)}.")
            continue

        return choice

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

options = [
    MenuOption("Start", start),
    MenuOption("View high scores", view_high_scores),
    MenuOption("View all questions", view_all_questions),
    MenuOption("Settings", view_settings),
    MenuOption("Credits", view_credits),
    MenuOption("Return to main menu", None),
]

def main_menu() -> None:
    """A while loop with user input and menu options"""
    while True:
        is_running = prompt_user_input(options, "CLI Terminal")
        if not is_running:
            break