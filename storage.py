#region start
"""
Read questions.json, read and write high_scores.json
"""
#endregion

import json


def read_questions():
    pass

def write_questions():
    pass

def write_high_scores():
    pass

def read_high_scores():
    pass

def write_file(file_name: str, lines: list[str]) -> None:
    try:
        with open(f"{file_name}.txt", 'w', encoding='utf-8') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("Trying to write a file inside a folder that does not exist...")
    except PermissionError:
        print("You do not have the system's permission to write to that specific location")
    except UnicodeEncodeError:
        print("The text you are trying to write contains characters that our chosen file encoding does not support")

def read_file(file_name: str) -> None:
    try: 
        with open(f"{file_name}.json", "r", encoding="utf-8") as file:
            file_name = json.load(file)

    except NameError:
        print("Name error: try again")

    print(len(file_name))

def load_questions(path) -> list:
    pass

def load_high_scores(path) -> list:
    pass

def save_high_scores(path, high_scores) -> None:
    pass