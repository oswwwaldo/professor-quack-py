import os

from dotenv import load_dotenv

import bot as discord_bot
import terminal


def main() -> None:
    load_dotenv()  
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
                print("Running the discord bot...")

                required_env = { 
                    'DISCORD_BOT_TOKEN': os.getenv('DISCORD_BOT_TOKEN'),
                    'TEST_SERVER_ID': os.getenv('TEST_SERVER_ID'),
                    'PROD_SERVER_ID': os.getenv('PROD_SERVER_ID')
                }

                missing = [label for label, secret in required_env.items() if not secret]

                if missing:
                    print(f"Missing environment variables detected, please provide values for: {', '.join(missing)}")
                else:
                    print("Token successfully loaded in...")
                    discord_bot.run_bot(required_env['DISCORD_BOT_TOKEN'], required_env['TEST_SERVER_ID'])

                while discord_bot.is_running:
                    pass

                print("Shutting the discord bot down...")
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