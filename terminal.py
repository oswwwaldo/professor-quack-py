#region start
"""
The terminal version (the core)
input(), while, import quiz.py functions 
"""
#endregion

import quiz
import storage

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
    return quiz.get_random_question(questions)

def quick_start() -> None:
    pass

def select_a_list() -> None:
    pass

def view_high_scores() -> None:
    pass

def view_credits() -> None:
    pass

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

def print_link(text: str, url: str, end: str = '\n') -> None:
    """Print a clickable URL to the terminal, supported by modern terminals — using the OSC 8 ANSI escape sequence"""
    print(f"\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\", end=end)

def print_credits() -> None:
    print("=" * 50)
    print('\n' * 1)
    print('Created by Oswaldo Fabrizio De Los Santos Ascencio')
    print(' ' * 6, end="")
    print_link("Visit the repository", "https://github.com/oswwwaldo/professor-quack-py/", end=" — ")
    print_link("Visit my Github", "https://github.com/oswwwaldo", end="")
    print(' ' * 6, end="")
    print('\n' * 1)
    print("=" * 50)

def main_menu() -> None:
    is_running: bool = True
    while is_running:
        print('\nCLI/Terminal:')
        print('[1] — Quick start')
        print('[2] — Select a list')
        print('[3] — View high scores')
        print('[4] — View all questions')
        print('[5] — Credits')
        print('[6] — Return to main menu')
        user_input = input("\nSelect an option (1-6)...").strip()

        match user_input:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                print_credits()
            case '6':
                is_running = False
                break
            case _:
                print("Invalid option, please choose (1-6).")