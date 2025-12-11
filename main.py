"""
Assistant Bot is the entry point to the application.

It launches an interactive console session for working with the address book:
- adding/editing/deleting contacts
- searching for phone numbers
- managing birthdays
- displaying upcoming birthdays
"""

from address_book import (
    AddressBook,
    parse_input,
    COMMANDS
    )


def main() -> None:
    """
    The main function of the bot.
    
    Loads the address book at startup,
    saves it when exiting,
    manages the entire user interaction cycle.
    """
    address_book = AddressBook.load_data()
    print("Welcome to the assistant bot!")
    while True:
        
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print('Enter a command please.')
            continue

        command, args = parse_input(user_input)

        if command not in COMMANDS:
            print('Invalid command.')
            continue
        
        result = COMMANDS[command](args, address_book)
        print(result)

        if command in ["close", "exit"]:
            address_book.save_data()
            break

if __name__ == '__main__':
    main()