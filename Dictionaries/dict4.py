user1 = {
    "name":"alice",
    "age":"25",
    "address":"45, Baker Street",
    "city":"London"
}

user2 = {
    "address2":"WB",
    "pincode":"700124566",
    "house:no":"m001245"
}

merge_user = user1 | user2
print("The new user :",merge_user)
