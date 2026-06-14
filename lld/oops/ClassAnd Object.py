class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        return f"My name is {self.name} and I am from {self.city}"

    def get_age(self):
        return self.age


s1 = Student("kp", "25", "Pune")
print(s1.display())
print(s1.get_age())
