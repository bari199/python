class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()    # inherited
d.bark()   # child method
