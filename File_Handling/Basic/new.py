name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write(name + "\n")
