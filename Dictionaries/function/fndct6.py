def add_user(userdata,name,user_id,age,number,gender):
    userdata[name]={
        "user_id":user_id,
        "age":age,
        "number":number,
        "gender":gender
    } 


def search_user(userdata, name):
    return userdata.get(name, "Contact not found")


userdata = {}

# Add multiple contacts
while True:
    name = input("Enter user name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    user_id = input("Enter user_id: ")
    age = input("Enter age:")
    number = input("Enter number:")
    gender = input("Enter gender:")

    add_user(userdata,name,user_id,age,number,gender)
# Search contacts by name (string)
while True:
    search_name = input("Enter name to search (or 'exit' to stop): ")
    if search_name.lower() == "exit":
        break
    print(search_name, ":", search_user(userdata, search_name))
