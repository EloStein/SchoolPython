class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

class Student(Person):
    def __init__(self, name, age, title):
        Person.__init__(self, name, age)
        self.title = title

    def smartGreet(self):
        print("Hello, my name is " + self.name + ", I am a " + self.title)

ole = Student("Ole", 16, "Ingenieur")
ole.smartGreet()