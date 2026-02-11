import os

directory_path = "D:\\Youtube\\"

if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")