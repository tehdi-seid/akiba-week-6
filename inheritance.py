class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programing_language):
        super().__init__(name, salary)
        self.programing_language = programing_language

    def display_info(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"programing_language: {self.programing_language}")


print("============= for employee ==============")
employee = Employee("spongbob", 8000)
employee.display_info()


print("============= for developer ==============")
developer = Developer("Tehdi seid", 10000, "python")
developer.display_info()


print("============= for manager ==============")
manager = Manager("panda", 40000, "software")
manager.display_info()

# inheritance is one of the pillars of oop it is the way that the child classes inherit the attribute and method of the parent class
# parent class is a class that is gonna being inherited but the child class is a class that is gonna inherit the attribute and methodsS
# overriding is the way that the child classes use the inherited method by changing the implementation but not the name of the method
# the purpose of supper() to initialize the inherited attributes inside the child class
# single inheritance is when one class inherits from one class but multiple inheritance when a class inherits form two classes
