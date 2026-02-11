class Student:
    school = "ABC School"   # Class Attribute

    def __init__(self, name, age):
        self.name = name    # Instance Attribute
        self.age = age

    def display(self):      # Method
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)


# Creating Objects
s1 = Student("Rahul", 20)
s2 = Student("Anita", 22)

# Calling Methods
s1.display()
print("-----")
s2.display()
