class bank:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

acc1=bank("John Doe",5000)
print("Account Holder:", acc1._name)
print("Balance:", acc1._balance)

class manager(bank):
    def __init__(self,name,balance,department):
        super().__init__(name,balance)
        self._department=department
manager1=manager("Alice",10000,"Sales")
print("Manager Name:", manager1._name)
print("Department:", manager1._department)
print("Balance:", acc1._balance)