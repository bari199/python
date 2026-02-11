products = {
    "apple":"65,000-inr",
    "nokia":"25,000-inr",
    "samsung":"45,000-inr",
    "oneplus+":"35,000-inr"
}
user={
    "name":"John Doe",
    "age":30,
    "city":"New York"
}




products2 = products.copy()
user.update({'age':28,'city':'Los Angeles'})
products2["samsung"]="50,000-inr"
print("Original Dictionary:", products2)
