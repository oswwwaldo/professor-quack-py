#region start
"""
Pure quiz logic: filter questions, check an answer, compute and format a score, rank high scores
"""
#endregion

import requests

url = "https://api.github.com/users/oswwwaldo"
response = requests.get(url)
data = response.json()
print(data['login'])
print(data["public_repos"])

def filter_questions(questions, difficulty, category):
    pass

def get_correct_letter(question):
    pass

def is_correct(question, letter):
    pass

def calculate_percent(correct, total):
    return (correct / total) * 100

def format_score(correct: int, total: int) -> str:
    return f"{(correct / total) * 100}%"

def is_high_score(percent, high_scores):
    pass

def add_high_score(high_scores, entry) -> list:
    pass