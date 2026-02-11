import os

# Current file name
current_name = "users.txt"

# New file name
new_name = "newfile.txt"

# Rename the file
os.rename(current_name, new_name)

print(f"File '{current_name}' renamed to '{new_name}' successfully.")