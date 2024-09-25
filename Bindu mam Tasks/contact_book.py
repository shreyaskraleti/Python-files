def display_menu():
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. View All Contacts")
    print("5. Exit")


def add_contact(contact_book):
    name = input("Enter the contact name: ")
    phone_number = input("Enter the phone number: ")

    if name in contact_book:
        print(f"Contact '{name}' already exists.")
    else:
        contact_book[name] = phone_number
        print(f"Contact '{name}' added successfully.")


def delete_contact(contact_book):
    name = input("Enter the contact name to delete: ")

    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' does not exist in the contact book.")


def search_contact(contact_book):
    name = input("Enter the contact name to search: ")

    if name in contact_book:
        print(f"Contact found: {name} - {contact_book[name]}")
    else:
        print(f"Contact '{name}' does not exist in the contact book.")


def view_all_contacts(contact_book):
    if not contact_book:
        print("No contacts found in the contact book.")
    else:
        print("=== All Contacts ===")
        for name, phone_number in contact_book.items():
            print(f"{name}: {phone_number}")
        print("====================")


def main():
    # Create an empty dictionary to store contacts
    contact_book = {}

    while True:
        # Display the menu
        display_menu()

        # Prompt the user to choose an option
        choice = input("Choose an option (1-5): ")

        # Handle the user's choice
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            delete_contact(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            view_all_contacts(contact_book)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Start the program
if __name__ == "__main__":
    main()
