class Parent:
    def parentMethod(self):
        a = 10
        b = 20
        print("Sum from parent method:", a + b)
class Child(Parent):
    def childMethod(self):
        x = 5
        y = 15
        print("Sum from child method:", x + y)
c = Child()

c.parentMethod()
c.childMethod()
#c.parentMethod()
