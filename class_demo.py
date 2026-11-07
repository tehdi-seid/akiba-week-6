print("============ class_demo ==============")
class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"name: {self.name}, \nstudent_id: {self.student_id}, \ndepartment: {self.department}")

    def introduce(self):
        print(f"hey, my name is {self.name}and my id is {self.student_id}, and my department is {self.department}")
student1=Student("Tehdi seid", "ru 8790/17", "software engineering")

student1.display_info()
student1.introduce()

student2=Student("seid muh", "ru 8790/17", "it")
student2.display_info()
student2.introduce()

student3=Student("you", "ru 8790/17", "python developer")
student3.display_info()
student3.introduce()

print("------------------------------------------")