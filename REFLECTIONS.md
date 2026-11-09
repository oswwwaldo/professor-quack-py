# Reflections.md

## Which project requirement did you find most challenging and how did you overcome this challenge? Be specific in your response

Code organization by far, I'm reading `A Philosophy of Software Design` and I'm working on intenralizing the book's ideas so it was insightful to see some of them apply as the codebase grew.

One glaring issue was how I initially organized my program in `main.py`. I used a `match` statement, hard-coded menu options and handled input, validation, question logic and more in each match case. This was a problem since it made bugfixing harder, scaling impossible and writing new features difficult since I had to constantly refer back to line 37 for a feature on line 195 for example.

I needed to shift from quick fixes to strategic design in this respect so I shifted to, for example, keeping all of my quiz-related logic that read `questions.json` in `quiz.py`.

A favorite of mine was when I built `prompt_user_input()`. It is meant to abstract the menu build/print process and the actual act of calling a dedicated controller (either typed input or arrow keys) and simply return an `int` so I could later check that against the menu's options and respond accordingly. This made it easy to create new menus without having to repeat any input, dispatch or error checking logic. The goal with each `prompt_user_input()` function call wasn't to demand for hyperspecific details and make me gloss over possible edge cases each time but to be 'common sense', general purposed and easy to read.

## Share one technical concept that you gained a deeper understanding of through building this project. Explain that concept in simple terms and explain how it is used in your project

I gained a deeper understanding of classes and type hints, especially `Callable`. In my project, I needed reusable menus in many places. Building each menu separately with hard-coded logic would make updates repetitive and difficult to maintain, I needed to create a menu in at least ten different places and I didn't want to make an edit ten different times just for one change.

I created a `MenuOption` class using `NamedTuple` to pair a `label` with an `action`. The `label` is a string, and the `action` is a `Callable`, which lets the program call the function associated with the option the user selects. Type hints make the intended structure clear and help catch mistakes when creating menu options.

Some options, such as “Return to main menu,” don’t need an action — so I typed the action as `Callable[[], object] | None` and gave it a default value of `None`. That means an action can be a no-argument function or None; when it is None, the menu handles it as an exit option.

## One additional reflection

As I was working on the `death_match` mode, I came across a very interesting and frustrating bug.

So the way `death_match` works, compared to `arcade` or `quick_start` is that `death_match` relies on wiping, redrawing the screen and listening for inputs constantly in order to mimic the feel of a timed question where only have 10s to answer.

The way I listened for inputs was by checking the blessed.keyboard.Keystroke object and verifying that against this qualifier:

```py
selected_answer: Keystroke = terminal.inkey(timeout=0.05)

if selected_answer.lower() in 'abcd':
```

The problem is that if there is no key collected (which is expected) the Keystroke returns an empty str -> ''.
But the in operator still counts this as true, in Python an empty string is in every string. In 'abcd', 'xyz' or '' — Python sees '' in all three string objects.

I just thought that was wild and needed to be said in the future.
