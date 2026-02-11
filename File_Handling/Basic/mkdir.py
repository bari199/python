import os

new_directory = "Oops2"

try:
   os.makedirs(new_directory)
   print(f"Directory '{new_directory}' created successfully.")
except OSError as e:
   print(f"Error: Failed to create directory '{new_directory}'. {e}")