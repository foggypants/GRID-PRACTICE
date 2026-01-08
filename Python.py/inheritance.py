class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    def show_manager(self):
        super().show_details()
        print("Role: Manager")
        print("Department:", self.department)
class Developer(Employee):
    def __init__(self, name, emp_id, roll_no):
        super().__init__(name, emp_id)
        self.roll_no = roll_no
    def show_developer(self):
        super().show_details()
        print("Role: Developer")
        print("Roll Number:", self.roll_no)
class Intern(Employee):
    def __init__(self, name, emp_id, duration):
        super().__init__(name, emp_id)
        self.duration = duration
    def show_intern(self):
        super().show_details()
        print("Role: Intern")
        print("Internship Duration (months):", self.duration)
'''
m1 = Manager("Alice", 1001, "Sales")
d1 = Developer("Bob", 2001, 101)
i1 = Intern("Charlie", 3001, 6)
print("== Manager Details ==")
m1.show_manager()
print("\n== Developer Details ==")
d1.show_developer()
print("\n== Intern Details ==")
i1.show_intern()
'''
employees = []
while True:
    print("\n=== Employee Menu ===")
    print("1.Add Manager")
    print("2.Add Developer")
    print("3.Add Intern")
    print("4.Show All Employees")
    print("5.Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        name = input("Enter name: ")
        emp_id = int(input("Enter employee ID: "))
        team_size = input("Enter department: ")
        emp = Manager(name, emp_id, team_size)
        print("\n== Manager Details ==")
        employees.append(emp)
        print("Manager added successfully!")
    elif choice == 2:
        name = input("Enter name: ")
        emp_id = int(input("Enter employee ID: "))
        roll_no = int(input("Enter roll number: "))
        emp = Developer(name, emp_id, roll_no)
        print("\n== Developer Details ==")
        employees.append(emp)
        print("Developer added successfully!")
    elif choice == 3:
        name = input("Enter name: ")
        emp_id = int(input("Enter employee ID: "))
        duration = int(input("Enter internship duration (months): "))
        emp = Intern(name, emp_id, duration)
        print("\n== Intern Details ==")
        employees.append(emp)
        print("Intern added successfully!")
    elif choice == 4:
        if not employees:
            print("No employees to show.")
        else:
            for emp in employees:
                print("\n-----------------------")
                if isinstance(emp, Manager):
                    emp.show_manager()
                elif isinstance(emp, Developer):
                    emp.show_developer()
                elif isinstance(emp, Intern):
                    emp.show_intern()
            
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
'''
print("Choose Employee Role")
print("1. Manager")
print("2. Developer")
print("3. Intern")
choice = int(input("Enter role (1-3): "))
if choice==1:
    team_size = int(input("Enter team size: "))
    name = input("Enter name: ")
    emp_id = int(input("Enter employee ID: "))
    emp = Manager(name, emp_id, team_size)
    print("\n== Manager Details ==")
    emp.show_manager()
elif choice==2:
    language = input("Enter programming language: ")
    name = input("Enter name: ")
    emp_id = int(input("Enter employee ID: "))
    emp = Developer(name, emp_id, language)
    print("\n== Developer Details ==")
    emp.show_developer()
elif choice==3:
    duration = int(input("Enter internship duration (months): "))
    name = input("Enter name: ")
    emp_id = int(input("Enter employee ID: "))
    emp = Intern(name, emp_id, duration)
    print("\n== Intern Details ==")
    emp.show_intern()
else:
    print("Invalid choice!")
'''