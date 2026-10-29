#region start
"""
Pure quiz logic: filter questions, check an answer, compute and format a score, rank high scores
"""
#endregion

import random


def get_questions(questions: list[dict]) -> list[dict]:
    """Return questions, note this may not be a useful function"""
    return questions
                
def get_question_by_id(questions: list[dict], id: str) -> dict | None:
    """Return a question by an id, returns none if none found""" # uses a generator expression combined with next()
    return next((question for question in questions if question['id'] == id), None)

def get_question_ids(questions: list[dict]) -> list[str]:
    """Return a list of all question ids"""
    return [question['id'] for question in questions]

def get_random_question(questions: list[dict]) -> dict:
    """Return a random question"""
    return random.choice(questions)

def get_random_questions(questions: list[dict], how_many: int = 10) -> list[dict]:
    """Return a given number amount of random questions in a list"""
    total_available = min(how_many, len(questions)) # returns the smallest, which would be len(questions) if the requested number is too large
    return random.sample(questions, total_available)

def filter_questions(questions: list[dict], difficulty: str | None, category: str | None) -> list[dict]:
    """Get questions by difficulty or category. Note to expand and add filtering by tags and source later"""

    if difficulty is None and category is None:
        raise ValueError("Sorry but you must attach a filter to this function, use `get_questions` instead for a full list ") 

    if difficulty and category:
        return [question for question in questions if question['difficulty'] == difficulty and question['category'] == category]
    
    elif difficulty:
        return [question for question in questions if question['difficulty'] == difficulty]

    elif category:
        return [question for question in questions if question['category'] == category]

    else:
        raise NameError("Somehow Palpatine returned...") # Just a simple check to see if we ever hit this error during execution

def get_all_categories(questions: list[dict]) -> list[str]:
    """Return a list of all categories within a question set with a set comprehension followed by sorted returning a list"""
    return sorted({question["category"] for question in questions})

def get_correct_letter(question: dict) -> str:
    """Return the correct answer in 'A', 'B', 'C' or 'D' of a question """
    answer = question['answer']
    for letter, choice in question['choices'].items():
        if choice == answer:
            return letter

def is_correct(question: dict, letter: str) -> bool:
    """Check whether the given letter is the correct answer to a question"""
    check_letter_is_valid(letter)
    return get_correct_letter(question) == letter.upper()

def check_letter_is_valid(letter: str) -> bool:
    """Validate letter as either A, B, C or D"""
    if len(letter) != 1 :
        raise ValueError("Please choose an answer: A, B, C or D")
    if letter.lower() not in 'abcd':
        raise ValueError(f"Your choice cannot be {letter!r}, it must either be A, B, C or D — please try again.")
    return True

def get_explanation(question: dict, letter: str) -> str:
    """Return the explanation of a question's letter choice, right or wrong"""
    check_letter_is_valid(letter)
    return question['explanations'][letter.upper()]

def calculate_percent(correct: int, total: int) -> float:
    """Return a float percentage based on two ints"""
    if total == 0:
        return 0
    return (correct / total) * 100

def format_score(correct: int, total: int) -> str:
    """Return a string, e.g 'Current score: 3/4 (75.00%)"""
    return f"Current score: {correct} / {total} ({calculate_percent(correct, total):.2f}%)"

def is_high_score(percent: int, high_scores: list[dict]) -> bool:
    pass

def add_high_score(high_scores: list[dict], entry: dict) -> None:
    pass