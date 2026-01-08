class InsufficientBalanceError(Exception):
    def __init__(self, balance):
        super().__init__(f"Insufficient FUNDS!!")


class ATMAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance)
        self.balance -= amount
        print(f"{amount} withdrawn succesfully")
        print(f"Remaining balance: {self.balance}")

try:
    account=ATMAccount(5000)
    account.withdraw(6000)
except Exception as e:
    print(e)

