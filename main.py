import api
import bot as discord_bot
import terminal
from terminal import MenuOption


def view_settings() -> None:
    options = [
        MenuOption("Switch to arrow-keys controller", terminal.activate_keys_controller),
        MenuOption("Switch to typed input controller", terminal.activate_input_controller),
        MenuOption("Return to main menu", None),
    ]

    while True:
        print('\n\n')
        if terminal.use_keys_controller is True:
            print("You are currently accessing the terminal via the arrow-keys interface")
        elif terminal.use_input_controller is True: 
            print("You are currently accessing the terminal via the typed input interface")
        else:
            print('Exception: else statement reached')
            print(f"use_keys: {terminal.use_keys_controller} && use_input: {terminal.use_input_controller}")

        terminal.print_menu("Welcome", options)
        terminal.print_divider("_")
        is_running = terminal.prompt_user_input(options)
        if not is_running:
            break

def prompt_view() -> None:
    options = [
        MenuOption("Start the terminal view", terminal.main_menu),
        MenuOption("Wake up the discord bot", discord_bot.main_menu),
        MenuOption("View API documentation", api.start),
        MenuOption("Settings", view_settings),
        MenuOption("Credits", terminal.view_credits),
        MenuOption("Quit", None),
    ]

    while True:
        terminal.print_menu("Main menu", options)
        terminal.print_divider("_")
        is_running = terminal.prompt_user_input(options)
        if not is_running:
            break

if __name__ == "__main__":
    print("\n\nWelcome —\n")
    prompt_view()