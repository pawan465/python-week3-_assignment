"""An OOP billing mini-project with a simple table-style receipt."""

from datetime import datetime
import random


class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=0.05):
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        self.tax_rate = tax_rate
        self.products = []
        self.bill_number = random.randint(1000, 9999)
        self.created_at = datetime.now()

    def add_product(self, product):
        self.products.append(product)

    def subtotal(self):
        return sum(product.line_total() for product in self.products)

    def tax(self):
        return self.subtotal() * self.tax_rate

    def total(self):
        return self.subtotal() + self.tax()

    def display(self):
        print("\n" + "=" * 62)
        print(f"BILL #{self.bill_number}     {self.created_at:%d %b %Y, %I:%M %p}")
        print("=" * 62)
        print(f"{'Product':<25}{'Price':>12}{'Qty':>8}{'Amount':>15}")
        print("-" * 62)
        for product in self.products:
            print(
                f"{product.name:<25}{product.price:>12.2f}"
                f"{product.quantity:>8}{product.line_total():>15.2f}"
            )
        print("-" * 62)
        print(f"{'Subtotal':>47}{self.subtotal():>15.2f}")
        print(f"{'Tax (' + format(self.tax_rate * 100, '.1f') + '%)':>47}{self.tax():>15.2f}")
        print(f"{'TOTAL':>47}{self.total():>15.2f}")
        print("=" * 62)


def main():
    bill = Bill(tax_rate=0.05)  # Change 0.05 to use a different 5% tax rate.
    print("BILLING SYSTEM - enter products one at a time.")
    while True:
        name = input("Product name (or press Enter to finish): ").strip()
        if not name:
            break
        try:
            price = float(input("Price in Rs.: "))
            quantity = int(input("Quantity: "))
            bill.add_product(Product(name, price, quantity))
            print("Product added.")
        except ValueError as error:
            print(f"Please try again: {error}")

    if bill.products:
        bill.display()
    else:
        print("No products were added, so no bill was created.")


if __name__ == "__main__":
    main()
