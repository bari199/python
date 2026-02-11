# List of lines to write to the file
lines = ["First line\n", "Second line\n", "Third line\n"]

# Open a file in write mode
with open("example.txt", "w") as file:
    file.writelines(lines)

print ("File opened successfully!!")