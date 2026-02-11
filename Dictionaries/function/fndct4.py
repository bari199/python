def add_contact(phonebook, name, number):
    phonebook[name] = number


def search_contact(phonebook, name):
    return phonebook.get(name, "Contact not found")


phonebook = {}

add_contact(phonebook, "Arif", "9876543210")
add_contact(phonebook, "Neha", "9123456789")

print(search_contact(phonebook, "Neha"))
print(search_contact(phonebook, "Aman"))
