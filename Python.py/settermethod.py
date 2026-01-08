class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance>=0:
            self.__balance=balance
        else:
            print("Invalid balance amount")

b=Bank(5000)
print("Initial Balance:", b.get_balance())