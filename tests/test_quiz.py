import quiz

SAMPLE_QUESTION = {
    "id": "test-001",
    "question": "What does `pwd` do?",
    "answer": "Prints the working directory",
    "choices": {
        "A": "Moves up a directory",
        "B": "Prints the working directory",
        "C": "Prints your password",
        "D": "Lists files",
    },
    "explanations": {
        "A": "That's `cd ..`.",
        "B": "Correct: print working directory.",
        "C": "Nothing to do with passwords.",
        "D": "That's `ls`.",
    },
    "difficulty": "easy",
    "category": "CLI",
}

SAMPLE_QUESTIONS = [
    SAMPLE_QUESTION,
    {**SAMPLE_QUESTION, "id": "test-002", "category": "Git", "difficulty": "hard"},
    {**SAMPLE_QUESTION, "id": "test-003", "category": "Git", "difficulty": "easy"},
] # the ** -> means -> copy every key and value from that dictionary into this one

def test_get_correct_letter():
    assert quiz.get_correct_letter(SAMPLE_QUESTION) == "B"

def test_get_question_by_id():
    assert quiz.get_question_by_id(SAMPLE_QUESTIONS, "test-001") == SAMPLE_QUESTION

def test_is_correct():
    assert quiz.is_correct(SAMPLE_QUESTION, "B") == True

def test_get_all_categories():
    assert quiz.get_all_categories(SAMPLE_QUESTIONS) == ["CLI", "Git"]

def test_calculate_percent():
    assert quiz.calculate_percent(3, 4) == 75
    assert quiz.calculate_percent(25, 50) == 50
    assert quiz.calculate_percent(0, 0) == 0
    assert quiz.calculate_percent(10000, 10000) == 100
    assert quiz.calculate_percent(0.5, 1) == 50