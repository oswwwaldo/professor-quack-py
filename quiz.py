#region start
"""
Pure quiz logic: filter questions, check an answer, compute and format a score, rank high scores
"""
#endregion

import random

# Follow YAGNI — you aren't going to need it 
# Follow DRY — don't repeat yourself
# Atomic pure functions with deep complexity over shallow


def print_question_ids(questions: list[dict]) -> None:
    """Print a list of question ids"""
    ids_list = [question['id'] for question in questions]
    print(*ids_list, sep='\n')

def get_questions(questions: list[dict]) -> list[dict]:
    return questions

def get_question_by_id(questions: list[dict], id: str) -> object:
    """Return a question by an id""" # uses a generator expression combined with next()
    return next((question for question in questions if question['id'] == id), None)

def get_question_ids(questions: list[dict]) -> list[str]:
    return [question['id'] for question in questions]

def get_random_question(questions: list[dict]) -> object:
    return random.choice(questions)

def filter_questions(questions: list[dict], difficulty: str, category: str) -> list[dict]:
    """Get questions by difficulty or category. Note to expand and add filtering by tags and source later"""

    if difficulty is None and category is None:
        raise NameError("Sorry but you attaach a filter to this function, use `get_questions` instead for a full list ") 
        return questions
    
    if difficulty:
        return [question for question in questions if question['difficulty'] == difficulty]

    if category:
        return [question for question in questions if question['category'] == category]

def get_all_categories(questions: list[dict]) -> list:
    seen_before = []
    for question in questions:
        if question['category'] not in seen_before:
            seen_before.append(question['category'])
    return seen_before

def get_all_categories(questions: list[dict]) -> list:
    return {question["category"] for question in questions}

def get_correct_letter(question: dict) -> str:
    answer = question['answer']
    for letter, choice in question['choices'].items():
        if choice == answer:
            return letter

def is_correct(question: dict, letter: str) -> bool:
    return get_correct_letter(question) == letter

def calculate_percent(correct: int, total: int) -> int:
    return (correct / total) * 100

def format_score(correct: int, total: int) -> str:
    return f"{calculate_percent(correct, total)}%"

def is_high_score(percent: int, high_scores: list[dict]) -> bool:
    pass

def add_high_score(high_scores: list[dict], entry: dict) -> None:
    pass