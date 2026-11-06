import api
import bot as discord_bot
import terminal
from terminal import MenuOption


def prompt_view() -> None:
    options = [
        MenuOption("Start the terminal view", terminal.main_menu),
        MenuOption("Wake up the discord bot", discord_bot.main_menu),
        MenuOption("View API documentation", api.start),
        MenuOption("Credits", terminal.view_credits),
        MenuOption("Quit", None),
    ]

    while True:
        terminal.print_menu("Welcome", options)
        terminal.print_divider("_")
        is_running = terminal.prompt_user_input(options)
        if not is_running:
            break

if __name__ == "__main__":
    prompt_view()