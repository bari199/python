def add_contact(phonebook, name, number):
    phonebook[name] = number


def search_contact(phonebook, name):
    return phonebook.get(name, "Contact not found")


phonebook = {}

# Add multiple contacts
while True:
    name = input("Enter name to add (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    number = input("Enter number: ")
    add_contact(phonebook, name, number)

# Search contacts by name (string)
while True:
    search_name = input("Enter name to search (or 'exit' to stop): ")
    if search_name.lower() == "exit":
        break
    print(search_name, ":", search_contact(phonebook, search_name))
