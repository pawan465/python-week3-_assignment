"""A small bank account example using classes and inheritance."""


class BankAccount:
    """Store an account owner's name and balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("There is not enough money in the account.")
        self.balance -= amount

    def display_balance(self):
        print(f"{self.owner}'s balance: Rs. {self.balance:.2f}")


class SavingsAccount(BankAccount):
    """A bank account that keeps a minimum balance."""

    def __init__(self, owner, balance=0, minimum_balance=500):
        super().__init__(owner, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        # This method overrides BankAccount.withdraw.
        if self.balance - amount < self.minimum_balance:
            raise ValueError(
                f"Keep at least Rs. {self.minimum_balance:.2f} in savings."
            )
        super().withdraw(amount)


if __name__ == "__main__":
    account = SavingsAccount("Asha", 2000)
    account.deposit(500)
    account.withdraw(300)
    account.display_balance()
