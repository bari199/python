# -----------------------------
# CLASS
# -----------------------------
# Class represents a blueprint of an Android Phone
class AndroidPhone:

    # -----------------------------
    # CONSTRUCTOR METHOD
    # -----------------------------
    # Purpose: Initialize attributes when object is created
    def __init__(self, brand, model, android_version, price):
        # ATTRIBUTES (Properties of Android Phone)
        self.brand = brand                 # phone brand (e.g., Samsung)
        self.model = model                 # phone model (e.g., Galaxy S23)
        self.android_version = android_version  # Android OS version
        self.price = price                 # phone price

    # -----------------------------
    # METHOD
    # -----------------------------
    # Purpose: Display phone details
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Android Version:", self.android_version)
        print("Price:", self.price)

    # -----------------------------
    # METHOD
    # -----------------------------
    # Purpose: Simulate calling feature
    def make_call(self, number):
        print(self.model, "is calling", number)


# -----------------------------
# OBJECT
# -----------------------------
# Object is a real-world instance of the class
phone1 = AndroidPhone(
    brand="Samsung",
    model="Galaxy S23",
    android_version="Android 14",
    price=75000
)

phone2 = AndroidPhone(
    brand="Google",
    model="Pixel 7",
    android_version="Android 13",
    price=60000
)


# -----------------------------
# USING METHODS WITH OBJECT
# -----------------------------
phone1.show_details()          # calling method
phone2.show_details()          # calling method
phone1.make_call("9876543210") # calling method
