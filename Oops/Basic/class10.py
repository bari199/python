class Student:
    school_name = "ABC School"   # class variable
    school_address = "123 Main Street"  # class variable

    @classmethod
    def show_school(cls):
        print(cls.school_name)
        print(cls.school_address)

Student.show_school()
