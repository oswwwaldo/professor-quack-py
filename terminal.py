#region start
"""
The terminal version (the core)
input(), while, import quiz.py functions 
"""
#endregion

import os
import shutil
import time
from dataclasses import dataclass
from collections.abc import Callable
from typing import NamedTuple

import readchar
from blessed import Terminal
from readchar import key

import quiz
import sound
import storage

term = Terminal()

# TODO: History related functions should be tied to a Player's object state
# A NamedTuple cannot change, a data class can
@dataclass
class Player:
    """Used to represent the player in leaderboards"""
    name: str = "Default user"
    username: str = "USER"
    country: Country = ("United States", "🇺🇸")
    high_score: int = 0

class Country(NamedTuple):
    """Used to represent a player's country in the leaderboards"""
    name: str
    flag: str

#region country list
# Countries and terrorities under the international country-code standard (ISO 3166-1)
COUNTRIES: list[Country] = [
    Country("United States", "🇺🇸"),
    Country("United Kingdom", "🇬🇧"),
    Country("Canada", "🇨🇦"),
    Country("Mexico", "🇲🇽"),
    Country("Brazil", "🇧🇷"),
    Country("France", "🇫🇷"),
    Country("Germany", "🇩🇪"),
    Country("India", "🇮🇳"),
    Country("Japan", "🇯🇵"),
    Country("Australia", "🇦🇺"),
 
    Country("Afghanistan", "🇦🇫"),
    Country("Åland Islands", "🇦🇽"),
    Country("Albania", "🇦🇱"),
    Country("Algeria", "🇩🇿"),
    Country("American Samoa", "🇦🇸"),
    Country("Andorra", "🇦🇩"),
    Country("Angola", "🇦🇴"),
    Country("Anguilla", "🇦🇮"),
    Country("Antarctica", "🇦🇶"),
    Country("Antigua and Barbuda", "🇦🇬"),
    Country("Argentina", "🇦🇷"),
    Country("Armenia", "🇦🇲"),
    Country("Aruba", "🇦🇼"),
    Country("Austria", "🇦🇹"),
    Country("Azerbaijan", "🇦🇿"),
    Country("Bahamas", "🇧🇸"),
    Country("Bahrain", "🇧🇭"),
    Country("Bangladesh", "🇧🇩"),
    Country("Barbados", "🇧🇧"),
    Country("Belarus", "🇧🇾"),
    Country("Belgium", "🇧🇪"),
    Country("Belize", "🇧🇿"),
    Country("Benin", "🇧🇯"),
    Country("Bermuda", "🇧🇲"),
    Country("Bhutan", "🇧🇹"),
    Country("Bolivia", "🇧🇴"),
    Country("Bosnia and Herzegovina", "🇧🇦"),
    Country("Botswana", "🇧🇼"),
    Country("Bouvet Island", "🇧🇻"),
    Country("British Indian Ocean Territory", "🇮🇴"),
    Country("British Virgin Islands", "🇻🇬"),
    Country("Brunei", "🇧🇳"),
    Country("Bulgaria", "🇧🇬"),
    Country("Burkina Faso", "🇧🇫"),
    Country("Burundi", "🇧🇮"),
    Country("Cambodia", "🇰🇭"),
    Country("Cameroon", "🇨🇲"),
    Country("Cape Verde", "🇨🇻"),
    Country("Caribbean Netherlands", "🇧🇶"),
    Country("Cayman Islands", "🇰🇾"),
    Country("Central African Republic", "🇨🇫"),
    Country("Chad", "🇹🇩"),
    Country("Chile", "🇨🇱"),
    Country("China", "🇨🇳"),
    Country("Christmas Island", "🇨🇽"),
    Country("Cocos (Keeling) Islands", "🇨🇨"),
    Country("Colombia", "🇨🇴"),
    Country("Comoros", "🇰🇲"),
    Country("Cook Islands", "🇨🇰"),
    Country("Costa Rica", "🇨🇷"),
    Country("Côte d'Ivoire", "🇨🇮"),
    Country("Croatia", "🇭🇷"),
    Country("Cuba", "🇨🇺"),
    Country("Curaçao", "🇨🇼"),
    Country("Cyprus", "🇨🇾"),
    Country("Czechia", "🇨🇿"),
    Country("Denmark", "🇩🇰"),
    Country("Djibouti", "🇩🇯"),
    Country("Dominica", "🇩🇲"),
    Country("Dominican Republic", "🇩🇴"),
    Country("DR Congo", "🇨🇩"),
    Country("Ecuador", "🇪🇨"),
    Country("Egypt", "🇪🇬"),
    Country("El Salvador", "🇸🇻"),
    Country("Equatorial Guinea", "🇬🇶"),
    Country("Eritrea", "🇪🇷"),
    Country("Estonia", "🇪🇪"),
    Country("Eswatini", "🇸🇿"),
    Country("Ethiopia", "🇪🇹"),
    Country("Falkland Islands", "🇫🇰"),
    Country("Faroe Islands", "🇫🇴"),
    Country("Fiji", "🇫🇯"),
    Country("Finland", "🇫🇮"),
    Country("French Guiana", "🇬🇫"),
    Country("French Polynesia", "🇵🇫"),
    Country("French Southern Territories", "🇹🇫"),
    Country("Gabon", "🇬🇦"),
    Country("Gambia", "🇬🇲"),
    Country("Georgia", "🇬🇪"),
    Country("Ghana", "🇬🇭"),
    Country("Gibraltar", "🇬🇮"),
    Country("Greece", "🇬🇷"),
    Country("Greenland", "🇬🇱"),
    Country("Grenada", "🇬🇩"),
    Country("Guadeloupe", "🇬🇵"),
    Country("Guam", "🇬🇺"),
    Country("Guatemala", "🇬🇹"),
    Country("Guernsey", "🇬🇬"),
    Country("Guinea", "🇬🇳"),
    Country("Guinea-Bissau", "🇬🇼"),
    Country("Guyana", "🇬🇾"),
    Country("Haiti", "🇭🇹"),
    Country("Heard and McDonald Islands", "🇭🇲"), # mc whopper
    Country("Honduras", "🇭🇳"),
    Country("Hong Kong", "🇭🇰"),
    Country("Hungary", "🇭🇺"),
    Country("Iceland", "🇮🇸"),
    Country("Indonesia", "🇮🇩"),
    Country("Iran", "🇮🇷"),
    Country("Iraq", "🇮🇶"),
    Country("Ireland", "🇮🇪"),
    Country("Isle of Man", "🇮🇲"),
    Country("Israel", "🇮🇱"),
    Country("Italy", "🇮🇹"),
    Country("Jamaica", "🇯🇲"),
    Country("Jersey", "🇯🇪"),
    Country("Jordan", "🇯🇴"),
    Country("Kazakhstan", "🇰🇿"),
    Country("Kenya", "🇰🇪"),
    Country("Kiribati", "🇰🇮"),
    Country("Kosovo", "🇽🇰"),
    Country("Kuwait", "🇰🇼"),
    Country("Kyrgyzstan", "🇰🇬"),
    Country("Laos", "🇱🇦"),
    Country("Latvia", "🇱🇻"),
    Country("Lebanon", "🇱🇧"),
    Country("Lesotho", "🇱🇸"),
    Country("Liberia", "🇱🇷"),
    Country("Libya", "🇱🇾"),
    Country("Liechtenstein", "🇱🇮"),
    Country("Lithuania", "🇱🇹"),
    Country("Luxembourg", "🇱🇺"),
    Country("Macau", "🇲🇴"),
    Country("Madagascar", "🇲🇬"),
    Country("Malawi", "🇲🇼"),
    Country("Malaysia", "🇲🇾"),
    Country("Maldives", "🇲🇻"),
    Country("Mali", "🇲🇱"),
    Country("Malta", "🇲🇹"),
    Country("Marshall Islands", "🇲🇭"),
    Country("Martinique", "🇲🇶"),
    Country("Mauritania", "🇲🇷"),
    Country("Mauritius", "🇲🇺"),
    Country("Mayotte", "🇾🇹"),
    Country("Micronesia", "🇫🇲"),
    Country("Moldova", "🇲🇩"),
    Country("Monaco", "🇲🇨"),
    Country("Mongolia", "🇲🇳"),
    Country("Montenegro", "🇲🇪"),
    Country("Montserrat", "🇲🇸"),
    Country("Morocco", "🇲🇦"),
    Country("Mozambique", "🇲🇿"),
    Country("Myanmar", "🇲🇲"),
    Country("Namibia", "🇳🇦"),
    Country("Nauru", "🇳🇷"),
    Country("Nepal", "🇳🇵"),
    Country("Netherlands", "🇳🇱"),
    Country("New Caledonia", "🇳🇨"),
    Country("New Zealand", "🇳🇿"),
    Country("Nicaragua", "🇳🇮"),
    Country("Niger", "🇳🇪"),
    Country("Nigeria", "🇳🇬"),
    Country("Niue", "🇳🇺"),
    Country("Norfolk Island", "🇳🇫"),
    Country("North Korea", "🇰🇵"),
    Country("North Macedonia", "🇲🇰"),
    Country("Northern Mariana Islands", "🇲🇵"),
    Country("Norway", "🇳🇴"),
    Country("Oman", "🇴🇲"),
    Country("Pakistan", "🇵🇰"),
    Country("Palau", "🇵🇼"),
    Country("Palestine", "🇵🇸"), # free palestine
    Country("Panama", "🇵🇦"),
    Country("Papua New Guinea", "🇵🇬"),
    Country("Paraguay", "🇵🇾"),
    Country("Peru", "🇵🇪"),
    Country("Philippines", "🇵🇭"),
    Country("Pitcairn Islands", "🇵🇳"),
    Country("Poland", "🇵🇱"),
    Country("Portugal", "🇵🇹"),
    Country("Puerto Rico", "🇵🇷"),
    Country("Qatar", "🇶🇦"),
    Country("Republic of the Congo", "🇨🇬"),
    Country("Réunion", "🇷🇪"),
    Country("Romania", "🇷🇴"),
    Country("Russia", "🇷🇺"),
    Country("Rwanda", "🇷🇼"),
    Country("Saint Barthélemy", "🇧🇱"),
    Country("Saint Helena", "🇸🇭"),
    Country("Saint Kitts and Nevis", "🇰🇳"),
    Country("Saint Lucia", "🇱🇨"),
    Country("Saint Martin", "🇲🇫"),
    Country("Saint Pierre and Miquelon", "🇵🇲"),
    Country("Saint Vincent and the Grenadines", "🇻🇨"),
    Country("Samoa", "🇼🇸"),
    Country("San Marino", "🇸🇲"),
    Country("São Tomé and Príncipe", "🇸🇹"),
    Country("Saudi Arabia", "🇸🇦"),
    Country("Senegal", "🇸🇳"),
    Country("Serbia", "🇷🇸"),
    Country("Seychelles", "🇸🇨"),
    Country("Sierra Leone", "🇸🇱"),
    Country("Singapore", "🇸🇬"),
    Country("Sint Maarten", "🇸🇽"),
    Country("Slovakia", "🇸🇰"),
    Country("Slovenia", "🇸🇮"),
    Country("Solomon Islands", "🇸🇧"),
    Country("Somalia", "🇸🇴"),
    Country("South Africa", "🇿🇦"),
    Country("South Georgia and the South Sandwich Islands", "🇬🇸"),
    Country("South Korea", "🇰🇷"),
    Country("South Sudan", "🇸🇸"),
    Country("Spain", "🇪🇸"),
    Country("Sri Lanka", "🇱🇰"),
    Country("Sudan", "🇸🇩"),
    Country("Suriname", "🇸🇷"),
    Country("Svalbard and Jan Mayen", "🇸🇯"),
    Country("Sweden", "🇸🇪"),
    Country("Switzerland", "🇨🇭"),
    Country("Syria", "🇸🇾"),
    Country("Taiwan", "🇹🇼"),
    Country("Tajikistan", "🇹🇯"),
    Country("Tanzania", "🇹🇿"),
    Country("Thailand", "🇹🇭"),
    Country("Timor-Leste", "🇹🇱"),
    Country("Togo", "🇹🇬"),
    Country("Tokelau", "🇹🇰"),
    Country("Tonga", "🇹🇴"),
    Country("Trinidad and Tobago", "🇹🇹"),
    Country("Tunisia", "🇹🇳"),
    Country("Türkiye", "🇹🇷"),
    Country("Turkmenistan", "🇹🇲"),
    Country("Turks and Caicos Islands", "🇹🇨"),
    Country("Tuvalu", "🇹🇻"),
    Country("U.S. Outlying Islands", "🇺🇲"),
    Country("U.S. Virgin Islands", "🇻🇮"),
    Country("Uganda", "🇺🇬"),
    Country("Ukraine", "🇺🇦"),
    Country("United Arab Emirates", "🇦🇪"),
    Country("Uruguay", "🇺🇾"),
    Country("Uzbekistan", "🇺🇿"),
    Country("Vanuatu", "🇻🇺"),
    Country("Vatican City", "🇻🇦"),
    Country("Venezuela", "🇻🇪"),
    Country("Vietnam", "🇻🇳"),
    Country("Wallis and Futuna", "🇼🇫"),
    Country("Western Sahara", "🇪🇭"),
    Country("Yemen", "🇾🇪"),
    Country("Zambia", "🇿🇲"),
    Country("Zimbabwe", "🇿🇼"),

    Country("European Union", "🇪🇺"),
    Country("United Nations", "🇺🇳"),

    Country("White flag", "🏳️"),
    Country("Black flag", "🏴"),
    Country("Transgender flag", "🏳️‍⚧️"),
    Country("Rainbow flag", "🏳️‍🌈"),
    Country("Triangular flag", "🚩"),
    Country("Pirate flag", "🏴‍☠️"),
    Country("Chequered flag", "🏁"),
    Country("Construction", "🚧"),
    Country("Duckland", "🪿")
]
#endregion

class MenuOption(NamedTuple):
    """Used to build menus, pairs a label and an action for returning a function to call"""
    label: str
    action: Callable[[], object] | None = None

Controller = Callable[[list[MenuOption], str], int] 
# Type-hinting shorthand for handle_keys/input_controllers

class Link(NamedTuple):
    """Used to print clickable links in the terminal, pairs a text and a url"""
    text: str
    url: str

MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 30

REQUIRED_USERNAME_LENGTH = 4

use_keys_controller: bool = False
use_input_controller: bool = True

player: Player = Player()
questions = storage.load_questions()
high_scores = storage.load_high_scores()

def ask_question(question: dict) -> str:
    """Prompts the user with a question, prints the menu and returns the user's returned letter choice"""

    letters = list(question['choices'].keys())
    options = [
        MenuOption(label, None)
        for label in question['choices'].values()
    ]

    call_controller = return_active_controller()
    user_input = call_controller(options, f"{question['id']} — {question['question']}")

    return letters[user_input - 1]  

def ask_to_continue(title: str = "What next?") -> bool:
    """Ask 'Next question / Return', prints the menu and returns True to keep playing"""
    options = [
        MenuOption("Next question", next_question),
        MenuOption("Return to terminal menu", None),
    ]
    
    return prompt_user_input(options, f"{title}")

def start() -> None:
    """Opens a menu with different game modes"""
    options = [
        MenuOption("Quick start", quick_start), # easiest way to get started
        MenuOption("Arcade", arcade), # allows you to pick which questions
        MenuOption("Death match", death_match), # only one life, this is eligible for high scores
        MenuOption("Return to terminal menu", None)
    ]

    while True:
        is_running = prompt_user_input(options, "START")
        if not is_running:
            break

#region game modes
#all game modes should store a history of correct and incorrect questions into another function
#should return a score
def quick_start() -> None:
    """Run quick start mode, immediately throwing a question for the user to answer randomly"""

    while True:
        length = 10
        round_questions = quiz.get_random_questions(questions, length)
        total_answered = 0
        correct = 0

        print(f"You'll be given {length} random questions based on the SWE Gitbook, goodluck!")
        
        for question in round_questions:
            total_answered += 1
            selected_answer = ask_question(question)
            result = quiz.format_result(question, selected_answer)
            print(result)

            if quiz.is_correct(question, selected_answer):
                correct += 1
                sound.play_correct()
            else:
                sound.play_wrong()
        
        score = quiz.format_score(correct, total_answered)
        print(f"You've scored: {score}")
        time.sleep(1.5)
        break

# TODO: Make it possible for a user to not have to choose a category or difficulty in the first place
def arcade() -> None:
    """Prompts the user for a category, difficulty and a length before returning a list of questions to answer"""
    while True:
        chosen_category: str = prompt_a_category()
        chosen_difficulty: str = prompt_a_difficulty()
        filtered_questions: list[dict] = quiz.filter_questions(questions, chosen_difficulty, chosen_category)

        if len(filtered_questions) < 1:
            print("That is so specific! No questions could be found under those qualifiers, please try again.")
            continue # restart the the while loop early

        chosen_length: int = prompt_a_length(filtered_questions)
        available_questions: list[dict] = quiz.get_random_questions(filtered_questions, chosen_length)

        total_answered: int = 0
        correct: int = 0

        print(f"You'll be given {chosen_length} questions in your filtered list! Enjoy {chosen_difficulty} {chosen_category}!")
        
        for question in available_questions:
            total_answered += 1
            selected_answer = ask_question(question)
            result = quiz.format_result(question, selected_answer)
            print(result)

            if quiz.is_correct(question, selected_answer):
                correct += 1
                sound.play_correct()
            else: 
                sound.play_wrong()

            if not ask_to_continue("Ready for another one?"):
                break
        
        score = quiz.format_score(correct, total_answered)
        print(f"You've scored: {score}")
        time.sleep(1.5)
        break

# TODO: Add more ascii examples, and a frozen set of acceptable strings to determine what 'mood' we want (i.e death, victory, wait etc)
def get_ascii_art(selection: int) -> str:
    """Returns one str from a collection of ASCII strings for dramatic effect"""
    ascii_art: list[str] = [
        """        
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⡟⠛⠛⠋⠉⠉⠉⠉⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠍⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠥⡍⡴⡃⠄⠒⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⠀⡀⡐⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠞⢼⢁⢇⠀⣄⠀⠀⠀⠀⠀⠀⠀⢠⠈⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢈⠔⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⠈⠐⠁⠅⢱⠊⡈⢩⡡⠀⠆⠁⠀⠀⠠⠐⠁⠀⢀⠀⠓⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠑⠺⠛⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠐⠀⠀⠀⠀⠂⣯⡋⠁⠁⠀⠁⠀⠀⢄⠀⠈⢧⠄⠀⠀⠀⢀⠐⣀⠠⠔⢊⡔⡀⣄⡀⠀⠈⢶⠆⣠⡀⢸⡔⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢀⠀⠈⠐⠄⢢⣴⣿⣦⣚⣂⡐⠌⢕⠀⡹⡀⡠⡀⠢⠔⠀⠐⠄⢘⣀⣩⣵⠒⡐⡟⠡⠀⡀⠠⢒⡈⢺⢝⣟⡐⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⠝⠀⠁⡈⣐⣽⣿⣿⣿⣟⣠⠰⣅⣢⣞⣡⣱⡮⠉⡠⢠⣀⣵⣾⣿⣿⣿⣿⣔⣶⡌⢲⣳⣬⠥⣎⣃⢋⢋⣿⣶⡨⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡇⠁⠀⢀⡢⠈⠉⠉⠉⠃⢛⢑⠛⠃⡦⡰⣋⣼⣌⣹⣁⣪⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⡁⢘⣺⣗⡌⣼⡛⢾⣿⣿⣿⣿⣧⣥⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣔⠕⠀⢀⠂⠀⡀⠀⠙⠤⠴⡒⠛⣿⣿⠟⠁⠙⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣽⠄⢁⣅⡌⠁⣨⣝⡹⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡇⠀⣶⢍⠄⠠⠀⠖⠀⠀⡀⠀⠀⡀⠉⢄⣟⡇⠁⠀⠀⠪⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⣡⡜⡜⡇⣾⣿⣿⣿⢹⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡇⣹⢿⡝⡆⡔⢁⠀⡆⠙⠡⠄⠀⠈⠀⠁⠘⣿⠀⠀⠀⠈⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⣃⡬⣾⠐⠁⣴⣿⣿⣿⣇⣆⣿⣿⣾⢏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣧⡘⠚⠁⡘⠀⢐⡖⢁⡖⠻⠠⣦⡁⠒⢨⣤⣿⠆⡀⡔⢀⠃⠀⡀⢁⢉⠌⠉⠀⠰⠐⣶⠻⢡⡟⠉⣰⣿⣿⣿⣿⣿⣧⣏⠛⠙⠿⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣯⠗⠌⠰⠀⢲⠃⠹⡝⠁⣃⣴⣿⠎⠜⠉⠐⠀⠀⠀⠀⠈⠠⠀⡱⣶⣮⣐⢈⡭⠆⣍⠶⠌⢧⠘⣾⣿⣿⣿⣿⣿⡏⡿⣘⢱⠭⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣟⡌⠰⠑⠀⠀⠆⡐⡠⣚⣾⠟⠀⠀⠑⠀⠀⠀⠀⠀⠩⢄⢀⠨⢶⠽⢨⣅⠛⢓⣥⡒⣨⠂⠀⡘⣿⣷⣿⣿⣿⣿⡗⡟⢻⢨⡣⣿⡌⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⣌⢭⣦⣱⣦⢰⣦⣌⢁⢲⡴⣀⣐⣀⡀⠀⠀⠀⠀⠏⠘⣶⣤⡀⠚⡯⠻⣏⢫⡟⢿⢀⢢⠱⠈⢛⡻⢿⡟⠿⡥⣃⡭⠤⢺⢽⢑⢽⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠻⣬⢋⠻⣿⣾⣿⣿⣾⣮⣧⣿⣿⣿⣷⣆⣤⡴⣦⣄⣐⣉⣙⠑⢄⢱⡂⢛⢜⡃⠈⠈⠘⡦⣒⠜⠗⢘⠧⢴⠷⢯⣃⣠⣾⣾⣮⣾⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⣋⢆⠒⠾⣿⣿⣿⣻⣿⣿⣿⣿⣿⢛⣛⣿⣿⣿⣧⣿⣿⡟⢮⠡⠈⢆⢈⢠⠋⡙⡇⢄⣉⠃⣧⡄⢳⡸⢌⢫⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠣⢡⠴⠹⢟⣶⣿⣽⣿⣿⣯⣽⣿⣿⡟⣻⣿⣿⣿⣿⡆⡼⢡⢣⣂⡇⠾⠇⠙⠃⡸⡌⢅⡑⠃⣀⠳⠡⠘⠶⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢚⢄⠋⣹⣿⡇⣹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣜⣼⡋⣄⣤⣶⣬⢷⣶⠇⢿⡟⠳⣾⢫⠻⡾⠛⣶⠳⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣎⡲⣠⡑⢻⣆⣟⠿⢻⣿⡏⠘⣿⣿⣿⣿⣿⣿⣻⠛⡻⢿⠋⢿⠙⡯⠠⣿⠈⠸⡇⡁⣫⢹⠀⡿⠃⢸⢩⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⡘⢧⡛⢛⣭⢪⢾⣿⣿⣯⣿⣿⣿⣷⣾⣿⣶⣾⣶⣿⣶⣿⣷⣿⣷⣾⣿⣶⣾⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡧⢀⠠⢿⡇⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠐⢠⡆⡈⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢐⡌⠑⡃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⢈⠠⠐⣆⠘⣻⣿⢋⣫⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢂⠁⠄⠺⡄⠓⣹⣷⣇⢀⡞⡹⠿⢿⢿⣿⣿⣿⣿⡯⣽⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⡂⠐⢀⠀⠁⣄⠐⠌⢍⠙⠳⡦⣿⡄⡟⢉⡏⠛⣹⢛⣿⠟⡟⢿⣩⡇⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣐⣐⠀⠀⠀⠈⢧⠜⠚⠕⠚⡄⢭⢙⠳⠿⣧⣶⠿⠦⡿⠾⠯⡿⠼⠷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠟⠂⠈⣯⢰⡅⡄⠏⠹⢁⠁⠂⠤⡄⡶⢰⡂⢯⠻⣟⢙⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣢⠄⡺⢧⡸⠘⣤⢠⠆⠈⠀⣁⡳⢦⡜⡃⢉⠻⣎⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⡀⠈⢃⠙⢤⠑⡆⡀⢇⢹⣏⢻⠃⠺⣇⡸⣘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠨⠃⠙⡼⠵⠺⠃⠀⠐⠈⠉⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⣀⣀⣀⣠⣴⣦⣬⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀""",
        """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣶⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢀⣈⣿⣶⣿⣿⣿⡿⢿⣿⡿⠛⠙⠻⣿⣿⡇⠀⠀
        ⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣆⣀⣤⣄⡀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⢀⣿⣿⣿⣿⡿⠿⠚⠀⢀⣾⣧⡀⠀⠀⠀⠀⠑⠄⠀
        ⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣜⠇⣇⠹⠋⠀⠀⠀⠀⢨⣿⠿⢦⡀⠀⠀⠀⠀⡀⠀
        ⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣿⣏⠀⠀⠀⠀⣀⣿⠇⠀⠀⢷⣆⣸⣀⣰⣿⣇
        ⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣷⣶⡾⢟⠁⠀⠀⢀⠀⣹⣟⡉⠀⠈⠻
        ⢀⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣤⣤⣴⣾⣿⣿⣾⡆⠀⠀⠀
        ⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠿⣿⣿⠁⠀⠀⠀⠀⢸⣿⣿⣿⠇⠀⠀⠙⣿⠛⢙⣛⠿⢿⣿⣿⣿⡯⠿⠿⠏⠏⢃⠀⠀⠀
        ⠀⢠⡏⠁⠀⠀⠀⠙⣻⣿⣿⣿⡿⠿⠻⠿⡛⡀⣾⣿⣦⣤⡄⣀⣀⣰⣿⠟⣿⣂⠀⠀⠀⣷⠀⣺⣿⣧⢈⣥⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢀⡆⢄⡄⠀⢀⣠⣴⣿⣿⣿⠿⠀⠀⠀⠀⠈⢣⣿⣿⣿⣿⣷⣿⣿⣿⣿⠀⢘⣿⣷⣶⣾⣿⡆⠸⠿⢿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢿⢿⣿⣷⣴⣿⣿⣿⠟⠁⢸⣧⡄⠀⠀⣀⣴⡷⠻⢿⣿⣿⣿⣿⣿⣿⣧⣠⣤⣿⣿⣿⣿⣿⣿⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢨⢻⣿⣿⣿⣿⣿⡃⢀⣀⢀⣯⣿⣿⣶⣿⣿⡇⠀⠀⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⣾⣯⣴⣿⣿⢿⣿⣿⡿⠃⠀⠀⠀⠘⢾⣿⡟⡿⠛⠛⠛⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠐⠿⠿⣿⢿⡿⢿⣿⣿⣿⣿⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    ]
    return ascii_art[selection]

def death_match() -> None:
    """One life, timed intensive mode—this is eligible for writing to high scores"""
    while True:

        clear_screen()
        print(get_ascii_art(0))
        time.sleep(1)

        print("This mode demands your absolute best, get as many questions right and be inducted into the hall of fame. Failure is not an option.")
        print("Answer as many as you can in ten seconds, you get 0.5s added on for every correct answer.")
        print("Chose incorrectly? You lose. Ran out of time? You lose.")
        time.sleep(1.5)
    
        options: list[MenuOption] = [
            MenuOption("I'm ready", next_question),
            MenuOption("I'm too chicken :C", None)
        ]
    
        call_controller: Callable = return_active_controller()
        user_input: int = call_controller(options, "This is a timed death match — are you ready?")


        if (user_input == 1):
            pass
        elif (user_input == 2):
            break
        else:
            continue

        total_answered: int = 0
        correct: int = 0

        clear_screen()
        print("The countdown starts now...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("0")
        time.sleep(0.5)

        available_questions: list[dict] = quiz.get_random_questions(questions, 50)

        for question in available_questions:
            
            total_answered += 1
            selected_answer = ask_question(question)
            # for seconds in [3, 2, 1]:
            #     print(f"\rTime left: {seconds}s ", end="", flush=True)
            #     time.sleep(1)
            #     print("\rTime's up!")
            
            result = quiz.format_result(question, selected_answer)
            print(result)

            if quiz.is_correct(question, selected_answer):
                correct += 1
                sound.play_correct()
            else:
                print(get_ascii_art(1))
                print("You died. You choose poorly.")
                sound.play_death()
                time.sleep(2)
                score = quiz.format_score(correct, total_answered)
                print(f"You've scored: {score}")
                time.sleep(1.5)
                if not ask_to_continue("Ready for another one?"):
                    break
        
        time.sleep(2)
        break
#endregion


def next_question() -> None:
    """A placeholder function for the quick_start menu so 'Next question' menu option has a callable"""

def add_easter_egg_menu_option(options: list[MenuOption]) -> tuple[list[MenuOption], str]:
    funny_phrases = [
        "Literally give me everything, I'm an absolute unit",
        "I'll take them all",
        "You want me to give you a range? Are you kidding?",
        "Imma yolo it",
        "Imma solo it",
        "LETSGOOOOOOOO",
        "The whole buffet. No plate left behind.",
        "Every question. I fear nothing.",
        "Gimme the entire question-verse.",
        "I'm about to become the question.",
        "All of them. The quiz is mine now.",
        "One question? Cute. Run me the whole gauntlet.",
        "Deploy the full question arsenal.",
        "I choose... yes.",
        "Maximum quiz. Engage.",
        "No brakes, just questions.",
        "The answer is: more questions.",
        "I'm speedrunning the entire database.",
        "Pour the questions directly into my brain.",
        "Release the quacken.",
    ]

    random_number: int = quiz.get_random_number(0, len(funny_phrases) - 1)
    message: str = funny_phrases[random_number]

    updated_options: list[MenuOption] = options.copy()
    updated_options.append(MenuOption(message))

    return updated_options, message


def prompt_a_length(questions: list[dict]) -> int:
    """Prompt the user for how many questions they'd like to answer, prints a menu and returns an int"""

    count: int = len(questions)
    counts: list[int] = [5, 10, 15]
    counts += list(range(25, count + 1, 10))

    options = [
        MenuOption(str(n))
        for n in counts
          if n <= count
    ]

    updated_options, easter_egg_label = add_easter_egg_menu_option(options)

    call_controller: Controller = return_active_controller()
    user_input: int = call_controller(updated_options, "Select the number of questions you'd like to practice for")
    user_choice: MenuOption = updated_options[user_input - 1]
    print(f"You selected: {user_choice.label}")

    # Assume easter egg label will prompt user to select all questions
    if user_choice.label == easter_egg_label:
        return len(questions)
    else:
        return int(user_choice.label)

def prompt_a_category() -> str:
    """Prompt the user for what category they'd like their questions in, prints a menu and returns an str"""
    all_categories: list[str] = quiz.get_all_categories(questions)

    options: list[MenuOption] = [
        MenuOption(label, None)
        for label in all_categories
    ]

    call_controller: Callable = return_active_controller()
    user_input: int = call_controller(options, "Select a category of questions to practice on")
    selected_category: MenuOption = options[user_input - 1]
    print(f"You selected: {selected_category.label}")

    return selected_category.label

# TODO: Note that prompt_a_difficulty may not return options sorted in this manner (easy -> med -> hard) but could be (easy -> hard -> med)
def prompt_a_difficulty() -> str:
    """Prompt the user for what difficulty they'd like to practice on, prints a menu and returns an str"""
    all_difficulty_modes: list[str] = quiz.get_all_difficulty_modes(questions)

    options: list[MenuOption] = [
        MenuOption(label, None)
        for label in all_difficulty_modes
    ]

    call_controller: Callable = return_active_controller()
    user_input: int = call_controller(options, "Select your difficulty to practice on")
    selected_difficulty_mode: MenuOption = options[user_input - 1]
    print(f"You selected: {selected_difficulty_mode.label}")

    return selected_difficulty_mode.label

def view_high_scores() -> None:
    print("View high scores called")

# TODO: Consider adding a time.sleep() to the menu build process
# ? This can probably be split into two functions considering there are two menus here
# ? Look into using quiz related functions instead
def view_all_questions(questions: list[dict] = questions) -> None:
    """Prompt the user into selecting a list of question ids to inspect its key-value pairs, handles two menus"""
    options: list[MenuOption] = [
        MenuOption(question["id"], None)
        for question in questions
    ]

    while True: 
        print(f"\n\nThis is a list of all the questions loaded: {len(questions)}, feel free to pick which one you'd like to inspect further")
        call_controller: Callable = return_active_controller()
        user_input: int = call_controller(options, "Question Browser")

        selected_question: dict = questions[user_input - 1]
        keys = list(selected_question.keys())

        question: list[MenuOption] = [
            MenuOption(key, None)
            for key in keys
        ]

        while True:
            user_input = call_controller(question, f"Inspecting {selected_question['id']}")
            selected_key: str = keys[user_input - 1]
            print(selected_question[selected_key])

            if not ask_to_continue("Would you like to go back?"):
                break

        print("\n\nQuestion Browser:")
        if not ask_to_continue("Would you like to return to the main menu or inspect another question?"):
            break

def view_settings() -> None:
    options = [
        MenuOption("Modify profile settings", view_profile),
        MenuOption("Toggle sound effects", sound.toggle_sfx),
        MenuOption("Toggle background music", sound.toggle_music),
        MenuOption("Return to main menu", None),
    ]
    while True:
        is_running = prompt_user_input(options, "CLI Terminal Settings")
        if not is_running:
            break

def view_profile() -> None:
    while True:
    options = [
            MenuOption(f"Name: {player.name}", change_name),
            MenuOption(f"Username: {player.username}", change_username),
            MenuOption(f"Country: {player.country.name}", change_country),
        MenuOption("Return to main menu", None),
    ]

        menu_title = "CLI: Profile Settings" # default title

        is_running = prompt_user_input(options, menu_title)
        if not is_running:
            break

def change_name() -> None:
    """Ask for a new player name and save it. Enter on an empty line keeps the current name"""
    while True:
        user_input = input(f"What would you like to be called? (currently {player.name}, Enter to cancel) ").strip()

        if user_input == "":
            print(f"No changes made. You're still {player.name}.")
            return

        if len(user_input) < MIN_NAME_LENGTH:
            print(f"Come on buddy, give us your REAL name (at least {MIN_NAME_LENGTH} characters).")
            continue

        if len(user_input) > MAX_NAME_LENGTH:
            print(f"Son... I ain't putting allat in ToT (keep it to {MAX_NAME_LENGTH} characters).")
            continue

        player.name = user_input
        print(f"Your name is now {player.name}.")
        return

def change_username() -> None:
    """Modifies the existing player object and changes their username, must be four letters in total for leaderboards"""
    while True:
        user_input = input(f"What would you like your user to be? Only {REQUIRED_USERNAME_LENGTH} characters please! (currently {player.name}, Enter to cancel) ").strip()

        if user_input == "":
            print(f"No changes made. You're still {player.username}.")
            return

        if len(user_input) is not REQUIRED_USERNAME_LENGTH:
            print(f"Sorry, try again! — at least {REQUIRED_USERNAME_LENGTH} characters).")
            continue

        player.username = user_input
        print(f"Your name is now {player.username}.")
        return

# TODO: Search functionality, build a search bar and return the Country object
def change_country() -> None:
    """Modifies the existing player object and changes their country"""

def view_credits() -> None:
    """View credits menu with three second delay"""
    print_credits()
    time.sleep(3)

def print_question_ids(questions: list[dict]) -> None:
    """Print a list of question ids"""
    ids_list = [question['id'] for question in questions]
    print(*ids_list, sep='\n')

def show_high_scores() -> None:
    pass

def centered_url(*links: Link, sep: str =" — ") -> str:
    """Return a centered string combining multiple Link objects"""
    texts = [text for text, url in links]
    result = centered(sep.join(texts))
    for text, url in links:
        result = result.replace(text, link(text, url))
    return result

def print_credits() -> None:
    """Print a menu of credits with clickable and centered links for flair"""
    print('\n' * 5)
    print_divider()
    print('\n' * 1)

    print(centered('Created by Oswaldo Fabrizio De Los Santos Ascencio'))
    print(
        centered_url( # A single function call with multiple Link objects
            Link(text="Visit my Github", url="https://github.com/oswwwaldo"),
            Link(text="Visit the repository", url="https://github.com/oswwwaldo/professor-quack-py"), 
            Link(text="Visit my LinkedIn", url="https://linkedin.com/oswwwaldo"),
        ) 
    )

    print('\n' * 1)
    print_divider()

def print_menu(title: str, options: list[MenuOption]) -> None:
    """Print a reuseable menu using the MenuOption class"""
    print(f'\n{title}:')
    for number, option in enumerate(options, start=1):
        print(f"[{number}] — {option.label}")
    print_divider("_")

def return_active_controller() -> Callable:
    """Returns the function handling the controller that is in use"""
    if (use_keys_controller is True):
        return handle_keys_controller
    elif (use_input_controller is True):
        return handle_input_controller
    else:
        raise NameError("No controller found in use")

def prompt_user_input(options: list[MenuOption], title: str = "") -> bool:
    """Let the user pick an option with the active controller and run it. Returns False when the option means 'leave'"""
    call_controller = return_active_controller()
    user_input = call_controller(options, title)
    chosen_menu_option = options[user_input - 1]

    if chosen_menu_option.action is None:
        return False

    chosen_menu_option.action()
    return True

#region print functions
def print_divider(char: str = "=") -> None:
    """Print a line of `char` that spans the terminal's current width via shutil"""
    width = shutil.get_terminal_size().columns
    print(char * width)

def centered(text: str, fill: str = " ") -> str:
    """Return a padded string object centered in the middle of the terminal window via shutil"""
    width = shutil.get_terminal_size().columns
    return text.center(width, fill)
    
def link(text: str, url: str, end: str = '\n') -> str:
    """Print a clickable URL to the terminal, supported by modern terminals — using the OSC 8 ANSI escape sequence"""
    return (f"\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\")
#endregion

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def handle_keys_controller(options: list[MenuOption], title: str = "" ) -> int:
    """Returns a menu option (int) via key-navigation using readchar and clear_screen"""
    selected = 0

    while True:
        clear_screen()
        print(f"{title}\n")
        for index, option in enumerate(options):
            marker = ">" if index == selected else " "
            print(f" {marker} {option.label}")

        pressed = readchar.readkey()

        if pressed == key.UP:
            selected = (selected - 1) % len(options)
        elif pressed == key.DOWN:
            selected = (selected + 1) % len(options)
        elif pressed in (key.ENTER, key.RIGHT):
            return selected + 1     

def handle_input_controller(options: list[MenuOption], title: str = "") -> int:
    """Returns a menu option (int) via typed input in the terminal"""
    print_menu(title, options)

    while True:
        user_input = input(f"\nSelect an option (1 - {len(options)})... ").strip()

        if not user_input.isdigit():
            print(f"Please enter a number from 1 to {len(options)}.")
            continue

        choice = int(user_input)
        if not 1 <= choice <= len(options):
            print(f"Please enter a number from 1 to {len(options)}.")
            continue

        return choice

def activate_keys_controller() -> None:
    """Switch to keys controller, disabling input controller"""
    global use_keys_controller
    global use_input_controller

    use_keys_controller = True
    use_input_controller = False
    print(f"The keys controller is now {use_keys_controller}")
    print(f"The input controller is now {use_input_controller}")

def activate_input_controller() -> None:
    """Switch to input controller, disabling keys controller"""
    global use_keys_controller
    global use_input_controller

    use_keys_controller = False
    use_input_controller = True
    print(f"The keys controller is now {use_keys_controller}")
    print(f"The input controller is now {use_input_controller}")

options = [
    MenuOption("Start", start),
    MenuOption("View high scores", view_high_scores),
    MenuOption("View all questions", view_all_questions),
    MenuOption("Settings", view_settings),
    MenuOption("Credits", view_credits),
    MenuOption("Return to main menu", None),
]

def main_menu() -> None:
    """A while loop with user input and menu options"""
    while True:
        is_running = prompt_user_input(options, "CLI Terminal")
        if not is_running:
            break