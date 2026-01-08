'''
class Student:
    def __init__(self,name,emp_id,attendance):
        self.name=name
        self.emp_id=emp_id
        self.attendance=0
    def Attendance(self):
        self.attendance+=1
        print("Attendance marked for", self.name)

    def details(self):
        print("-------- Employee Details --------")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Total Attendance:", self.attendance)
    
s1=Student("John Doe", 101, 0)
s2=Student("Jane Smith", 102, 0)
s3=Student("Alice Johnson", 103, 0)

'''
class person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Name:",self.name)
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        print("Roll No:",self.roll)

s1=student("John",101)
s1.show()
s1.display()
s2=person("Alice")
s2.show()
s2.display()
