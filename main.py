"""
# Core: multiple-choice questions, score functionality (“2/3 (67%)”), high score, and a top-5 high score board to JSON

# Categories and difficulty: add fields to each question dict and filter the list

# Timer: (discord.py) view ontimeoutmethod 

# Announcements: (discord.ext.tasks) (a loop that checks dates and board information once a day). 

# Code challenger: CodeWars, HackerRank etc.

# PR reviewer: needs GitHub webhooks or the API

Pydantic, Docker, pytest, Github Action

QuizAPI.io

Anki
"""

import os

from dotenv import load_dotenv

load_dotenv()  
token = os.getenv("DISCORD_TOKEN")

if not token:
    print("Missing DISCORD_TOKEN. Copy .env.example to .env and add your token.")
else:
    print("Token successfully loaded in")
    # client.run(token)