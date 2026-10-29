#region start
"""
Read questions.json, read and write high_scores.json
"""
#endregion

import json


def write_file(file_name: str, lines: list[str]) -> None:
    try:
        with open(f"{file_name}", 'w', encoding='utf-8') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("Trying to write a file inside a folder that does not exist...")
    except PermissionError:
        print("You do not have the system's permission to write to that location")
    except UnicodeEncodeError:
        print("The text you are trying to write contains characters that our chosen file encoding does not support")

def read_file(file_name: str) -> None:
    try: 
        with open(f"{file_name}", "r", encoding="utf-8") as file:
            json_file = json.load(file)
            print(f'Lines loaded: {len(json_file)}')
            return json_file

    except NameError:
        print("Name error: try again")
    except FileNotFoundError:
        print("Trying to read a file that does not exist")
    except PermissionError:
        print("You do not have the system's permission to read that location")
    except UnicodeEncodeError:
        print("The text you are trying to read contains characters that our chosen file encoding does not support")

def load_questions(file_name: str = 'questions.json') -> list[dict]:
    try:
        json_file = read_file(file_name)
    except json.JSONDecodeError:
        print('This file exists but is not a valid JSON file')

    return json_file

def load_high_scores(file_name: str = 'high_scores.json') -> list[dict]:
    try:
        json_file = read_file(file_name)
    except json.JSONDecodeError:
        print('This file exists but is not a valid JSON file')

    return json_file

def save_high_scores(file_name: str = 'high_scores.json', high_scores: list | None = None, ) -> None:
    if high_scores is None:
        high_scores = []

    
    