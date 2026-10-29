import requests
from fastapi import FastAPI

import quiz
import storage

app = FastAPI()

try:
    questions = storage.load_questions()
    high_scores = storage.load_high_scores()
except NameError:
    ("JSON data storage was not found")

@app.get("/")
def index(name: str | None = None):
    return f"Hello {name or 'world'}!"
    
@app.get('/credits')
def get_github() -> dict: 
    url = "https://api.github.com/users/oswwwaldo"
    response = requests.get(url)
    data = response.json()
    return data

@app.get('/all-categories')
def all_categories() -> list[str]:
    return quiz.get_all_categories(questions)

@app.get('/all-ids')
def all_ids() -> list[str]:
    return quiz.get_question_ids(questions) 