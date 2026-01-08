class Bank:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance
    def get_balance(self):
        return self.__balance
b=Bank("John Doe", "123456789", 5000)
print("Balance:", b.get_balance())
'''
class Manager(Bank):
    def __init__(self, name, acc_no, balance, department):
        super().__init__(name, acc_no, balance)
        self.department = department
manager1 = Manager("Alice", "987654321", 10000, "Sales")
print("Manager Name:", manager1.name)
print("Department:", manager1.department)
print("Balance:", manager1._balance)
print("Account Number:", manager1.acc_no)

'''