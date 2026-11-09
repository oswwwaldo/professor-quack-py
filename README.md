# Professor Quack.py

A quiz app for Marcy Lab School SWE students based on the 2026 Gitbook, available in three branches—as a CLI application, as a Discord bot or as an API.

Eventually this quiz app will expand to new technologies, languages and tooling.

Please note for grading purposes, only interact with the CLI terminal view. Furthermore, a lot of features were attempted and some at varying states of completion.

## Installation

Having issues getting this repository set up? Refer to this quick walk-through, if you are still experencing problems feel free to create an issue in the repository  and report your problem!

### Requirements

- Python 3.12 or newer (developed on Python 3.14)
- Git

### 1. Clone the repository and move into it

   ```bash
   git clone https://github.com/oswwwaldo/professor-quack-py.git
   cd professor-quack-py
   ```

### 2. Create and activate a virtual environment

   Windows (PowerShell)

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   macOS / Linux

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

### 3. Install the dependencies

   ```bash
   python -m pip install -r requirements.txt
   ```

### 4. Profit

![An image of great happiness](profit.jpg)

## Running the quiz

```bash
python main.py
```

On macOS or Linux, use `python3` if `python` isn't found.

Choose options by typing their number and pressing Enter. To use the arrow keys instead, open **Settings** and switch controllers. Arrow-key mode works in most modern terminals, including Windows Terminal and VS Code's terminal though keep in mind that this mode is not fully supported yet.

## Running the tests

```bash
python -m pytest
```

## Discord bot (optional)

To run the Discord bot, copy `.env.example` to `.env` and fill in your bot token and server IDs. The file explains where to find each value.

Keep in mind this is a pending feature that is not ready for playtesting.

## FastAPI server (optional)

To start the API view specifically, please run `uvicorn api:app --reload`

Keep in mind this is a pending feature that does not represent the intended finished product

## Why is this repository called Professor Quack.py?

Because.

## What is this project?

It is a quiz application meant to help fellows at the Marcy Lab School learn more about Gitbook-covered material. The questions were generated using Claude to be relevant and on varying degrees of difficulty and categories.

I am still looking into whether this project could be genuinely useful for my target audience but in the future I think I'd like to add some kind of physical station with a Raspberry Pico machine. The API porition of this project is an endpoint for that machine to work with over the internet and the discord bot is meant to be a friendly and easy way to get into 'Professor Quack'.

I will look into conducting qualitive surveys and interviews to gauge how much of an investment this project should cost me over my year at the Marcy Lab.

## Design principles

- YAGNI — you aren't going to need it

- DRY — don't repeat yourself

- Atomic pure functions

- Write deep modules with rich functionality hidden behind simple and shallow interfaces

- Common sense and prioritize common use cases

A function earns its place when it... names an intent, hides an edge case, is testable and gives you one place to change behavior

## Overview

![Architecture](Untitled-2026-11-7-1632.png)

The app communicates either as a CLI terminal application, discord bot or as an API. All three views have slightly different functionality.

## Features for the future

- Track question history (build a list of correct/incorrect questions).

### Core

- Multiple-choice questions
- Score display (for example, `2/3 (67%)`)
- High score tracking
- Top-five high score board saved to JSON
- Show answered questions
- Show answered correctly questions
- Show answered incorrectly questions

### Categories and Difficulty

- Add category and difficulty fields to each question dictionary.
- Filter the question list by category and difficulty.
- Remove questions from review/study

### Timer

- Use the `discord.py` view `on_timeout` method.

### Announcements

- Use `discord.ext.tasks` to run a loop once a day.
- Check dates and leaderboard information.
- Post updates in the respective channel:
  - F26 SWE Landing Page → `#all-swe`
  - Allagi L&D Landing Page → `#swe-allagi`
  - Coaching Landing Page → `#swe-telos`

### Code Challenges

- Codewars, HackerRank, etc.

### Pull Request Reviewer

Exclusively on the Discord bot, this would help fellows find people to review their code on discord.

- GitHub webhooks or API

### Explain Code

- Google AI Studio API calls

### Technologies and Tools

- Pydantic
- pytest
- GitHub Actions
- FastAPI
- Docker
- Google AI Studio
- Cloudflare Workers

- Anki (FSRS)
- QuizAPI.io

## Planned Slash Commands

- `/help`
- `/quiz`
- `/rankings`
- `/review`
- `/board`
- `/explain`
- `/quack`

## Source TO Pull From

[Google Doc](https://docs.google.com/document/d/1HDtu0-PQcvYO4X-RIxT8mjOcsxf3cgXGdFPtXZN7QDM)
