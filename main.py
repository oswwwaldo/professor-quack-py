import os

from dotenv import load_dotenv

import bot as discord_bot


def main() -> None:
    load_dotenv()  
    prompt_view()

def prompt_view() -> None:
    while True:
        print('\nWelcome:')
        print('[1] — Start the terminal quiz')
        print('[2] — Wake up the discord bot')
        print('[3] — Credits')
        print('[4] — Quit')
        user_input = input("\nSelect an option (1-4)...").strip()

        match user_input:
            case '1':
                print('Starting up the CLI...')
            case '2':
                print("Running discord...")

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
            case '3':
                print("Credits...")
            case '4':
                print("Quitting program...")
                break 
            case _:
                print("Invalid option, please choose (1-4).")

if __name__ == "__main__":
    main()