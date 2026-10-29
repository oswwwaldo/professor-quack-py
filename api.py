import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index(name: str | None = None):
    return f"Hello {name or 'world'}!"
    
@app.get('/credits')
def get_github() -> dict: 
    url = "https://api.github.com/users/oswwwaldo"
    response = requests.get(url)
    data = response.json()
    return data
