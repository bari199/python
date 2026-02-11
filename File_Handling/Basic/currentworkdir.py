import os

current_directory = os.getcwd()

if current_directory == "E:\\python":
    print("The files is exists.")
else:
    print("The files is not exists.")

print(f"Current working directory: {current_directory}")