# Professor Quack.py

A discord bot with quiz, pull request matchmaking, code challenging and LLM functionality. It's a bot with a personality—he's also a duck.

## Overview

![Architecture](Untitled-2026-10-26-1632.png)

The app communicates either as a CLI terminal application or as a discord bot (with added functionality)

## Core

- Multiple-choice questions
- Score display (for example, `2/3 (67%)`)
- High score tracking
- Top-five high score board saved to JSON
- Show answered questions
- Show answered correctly questions
- Show answered incorrectly questions

## Categories and Difficulty

- Add category and difficulty fields to each question dictionary.
- Filter the question list by category and difficulty.
- Remove questions from review/study

## Timer

- Use the `discord.py` view `on_timeout` method.

## Announcements

- Use `discord.ext.tasks` to run a loop once a day.
- Check dates and leaderboard information.
- Post updates in the respective channel:
  - F26 SWE Landing Page → `#all-swe`
  - Allagi L&D Landing Page → `#swe-allagi`
  - Coaching Landing Page → `#swe-telos`

## Code Challenges

- Codewars, HackerRank, etc.

## Pull Request Reviewer

- GitHub webhooks or API

## Explain Code

- Google AI Studio API calls

## Technologies and Tools

- Pydantic
- Docker
- pytest
- GitHub Actions
- Google AI Studio
- Cloudflare Workers
- Anki
- QuizAPI.io

## Answer Matching

- Use the Levenshtein algorithm to handle possible answer mismatches, such as extra whitespace in a question or answer.

## Slash Commands

- `/help`
- `/quiz`
- `/rankings`
- `/review`
- `/board`
- `/explain`
- `/quack`

## Source

[Google Doc](https://docs.google.com/document/d/1HDtu0-PQcvYO4X-RIxT8mjOcsxf3cgXGdFPtXZN7QDM)
