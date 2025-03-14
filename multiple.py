class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Worker:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary
    
    def work_info(self):
        return f"I work as a {self.job_title} and earn ${self.salary} per year."


class Manager(Person, Worker):
    def __init__(self, name, age, job_title, salary, team_size):
        Person.__init__(self, name, age)
        Worker.__init__(self, job_title, salary)
        self.team_size = team_size
    
    def manager_info(self):
        return f"I manage a team of {self.team_size} people."

manager = Manager("Alice", 35, "Project Manager", 85000, 10)

print(manager.greet())
print(manager.work_info())
print(manager.manager_info())


