'''
username=input("Enter username: ")
if len(username)>8 and any(char in "!@#$$%" for char in username):
    print("Username created successfully.")
else:
    raise ValueError("Username must be longer than 8 characters and contain at least one special character (!,@,#,$,%)")
password=(input("Enter password: "))

def login(user, pwd):
    def login(user, pwd):
        if user == username and pwd == password:
            print("Login successful!")
        else:
            raise ValueError("Invalid username or password")
login(username, password)
def try_login():
    user=input("Enter username to login: ")
    pwd=input("Enter password to login: ")
    try:
        login(user, pwd)
    except ValueError as ve:
        print(ve)
try_login()

def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()


import time 
def logger(func):
    def wrapper():
        start_time = time.time()
        print("[LOG] process_data started")
        print("Processing data...")
        func()
        end_time = time.time()
        print("[LOG] process_data finished")
        duration = end_time - start_time
        print(f"[LOG] Duration: {duration:.2f} seconds")
    return wrapper
@logger
def process_data():
    time.sleep(1)
    print("Data processed successfully.")
process_data()

def report(func):
    def wrapper():
        start_time = time.time()
        print("[LOG]generate_report started")
        print("Generating report...")
        func()
        end_time = time.time()
        print("[LOG] generate_report finished")
        duration = end_time - start_time
        print(f"[LOG] Duration: {duration:.2f} seconds")
    return wrapper
@report
def generate_report():
    time.sleep(2)
generate_report()
 

class Student:
    name=""
    emp_ID= 0
    emp_salary=0.0
    Company_name="ABC Corp"
    def display(self):    
        print("Name: ",self.name)
        print("Emp_ID: ",self.emp_ID)
        print("Emp_Salary: ",self.emp_salary)
        print("Company_name: ",self.Company_name)
s1=Student()
s1.name=input("Enter name: ")
s1.emp_ID=int(input("Enter employee ID: "))
s1.emp_salary=float(input("Enter employee salary: "))
s1.Company_name=input("Enter company name: ")
s1.display()
s2=Student()
s2.name=input("Enter name: ")
s2.emp_ID=int(input("Enter employee ID: "))
s2.emp_salary=float(input("Enter employee salary: "))
s2.Company_name=input("Enter company name: ")
s2.display()

class Student:
    college="ABC College"

    def __init__(self, name):
        self.name=name

s1=Student("Amit")
s2=Student("Sonia")

print(s1.college)
print(s2.college)
Student.college="XYZ College"
print(s1.college)
print(s2.college)


'''
class Student:
    def __init__(self, name, roll_no,m1, m2, m3):
        self.name = input("Enter name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.m1 = int(input("Enter marks for subject 1: "))
        self.m2 = int(input("Enter marks for subject 2: "))
        self.m3 = int(input("Enter marks for subject 3: "))
        total = self.m1 + self.m2 + self.m3
        percentage = round(total / 3, 2)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)

s1=Student(None, None, None, None, None)
def showreport():
    print("Report generated for", s1.name)
showreport()