import os

# File to be deleted
file_to_delete = "seventh.pdf"

# Delete the file
os.remove(file_to_delete)

print(f"File '{file_to_delete}' deleted successfully.")