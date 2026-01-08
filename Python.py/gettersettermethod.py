class Bank:
    def __init__(self, name, acc_no, balance, acc_holder):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount<=0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)
    def show_account(self):
        print("\n-----Bank Account Details-----")
        print("Account Holder:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.__balance)
name=input("Enter account holder name: ")
acc_no=input("Enter account number: ")
balance=float(input("Enter initial balance: "))
acc_holder=input("Enter account holder type (Personal/Business): ")
b=Bank(name, acc_no, balance, acc_holder)
b.show_account()
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Account Details")
    print("4. Exit")
    choice=input("Enter your choice (1-4): ")
    if choice=="1":
        amount=float(input("Enter amount to deposit: "))
        b.deposit(amount)
    elif choice=="2":
        amount=float(input("Enter amount to withdraw: "))
        b.withdraw(amount)
    elif choice=="3":
        b.show_account()
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")