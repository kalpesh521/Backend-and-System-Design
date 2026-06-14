class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"name is {self.name} and salary is {self.salary}"

    def get_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def __init__(self, name, salary ,team_size):
        super().__init__(name, salary)
        self.team_size =team_size

    def get_bonus(self):
        return self.salary * 0.20 + (self.team_size * 500)

    def get_details(self):
        base = super().get_details()
        return f"{base} | Team {self.team_size} members"


m = Manager("kp",200000 ,10)
print(m.get_bonus())
print(m.get_details())
