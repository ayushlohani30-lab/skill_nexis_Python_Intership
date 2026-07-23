# Contact Book using Dictionary

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"'{name}' already exists! Use update option to change the number.")
        return
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")

def search_contact():
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Name: {name} | Phone: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        contacts[name] = new_phone
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def display_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\n--- ALL CONTACTS ---")
        for name, phone in contacts.items():
            print(f"Name: {name:<15} | Phone: {phone}")

def main():
    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()