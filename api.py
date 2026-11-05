import threading
import webbrowser

import requests
import uvicorn
from fastapi import FastAPI

import quiz
import storage

app = FastAPI()

def start():
    print('Loading API endpoints...')
    loopback_address:str = '127.0.0.1'
    port:str = '8000'
    threading.Timer(2, open_browser, args=None).start() # Queue the open_browser call by 2 seconds so uvicorn has time to start up first
    uvicorn.run('api:app', host=loopback_address, port=port)

def open_browser() -> None:
    webbrowser.open('http://127.0.0.1:8000/docs')

questions = storage.load_questions()
high_scores = storage.load_high_scores()

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

@app.post('/post')
def post():
    pass

@app.put('/put')
def put():
    pass

@app.delete('/delete')
def delete():
    pass