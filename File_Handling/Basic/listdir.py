import os

directory_path = r"E:\Oops"
try:
   contents = os.listdir(directory_path)
   print(f"Contents of '{directory_path}':")
   for item in contents:
      print(item)
except OSError as e:
   print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")