#region start
"""
Pure quiz logic: filter questions, check an answer, compute and format a score, rank high scores
"""
#endregion

import random
import requests

import storage

url = "https://api.github.com/users/oswwwaldo"
response = requests.get(url)
data = response.json()
print(data['login'])
print(data["public_repos"])


def print_question_ids():
    ids_list = []
    dicts_list = storage.load_questions()
    for dict in dicts_list:
        ids_list.append(dict['id'])
    print(*ids_list, sep='\n')

# print_question_ids()

def get_question_by_id(id: str) -> object:
    return 

def get_questions_by_tags(tags: str) -> list[dict]:
    pass

def get_questions_by_category(category: str) -> list[dict]:
    pass

def get_questions_by_difficulty(difficulty: str) -> list[dict]:
    pass

def get_questions_by_source(source: str) -> list[dict]:
    pass

def get_question_ids() -> list[str]:
    ids_list = []
    dicts_list = storage.load_questions()
    for dict in dicts_list:
        ids_list.append(dict['id'])
    return ids_list

def get_random_question() -> object:
    dicts_list = storage.load_questions()
    random_number = random.randint(0, len(dicts_list))
    random_question = dicts_list[random_number]
    return random_question

def filter_questions(questions, difficulty, category) -> list[dict]:
    pass

def get_correct_letter(question) -> str:
    answer = question['answer']
    for letter, choice in question['choices'].items():
        if choice == answer:
            return letter

def is_correct(question, letter) -> bool:
    return get_correct_letter(question) == letter

def calculate_percent(correct, total) -> int:
    return (correct / total) * 100

def format_score(correct: int, total: int) -> str:
    return f"{calculate_percent(correct, total)}%"

def is_high_score(percent, high_scores) -> bool:
    pass

def add_high_score(high_scores, entry) -> None:
    pass