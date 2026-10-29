import bot as discord_bot
import terminal


def main() -> None:
    prompt_view()

def prompt_view() -> None:
    while True:
        print('\nWelcome:')
        print('[1] — Start the terminal view')
        print('[2] — Wake up the discord bot')
        print('[3] — View API documentation')
        print('[4] — Credits')
        print('[5] — Quit')
        user_input = input("\nSelect an option (1-4)...").strip()

        match user_input:
            case '1':
                terminal.main_menu()
            case '2':
                discord_bot.main_menu()
            case '3':
                print("Opening API documenation...")
            case '4':
                terminal.print_credits()
            case '5':
                print("Quitting program...")
                break 
            case 'exit':
                break
            case _:
                print("Invalid option, please choose (1-4).")

if __name__ == "__main__":
    main()