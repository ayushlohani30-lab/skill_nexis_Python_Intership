# OOP-based Billing System using datetime for dynamic invoice timestamps

from datetime import datetime
from typing import List

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def calculate_item_total(self) -> float:
        return self.price * self.quantity


class Bill:
    def __init__(self, customer_name: str, tax_rate_percent: float = 5.0):
        self.customer_name = customer_name
        self.tax_rate_percent = tax_rate_percent
        self.items: List[Product] = []
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_product(self, product: Product):
        self.items.append(product)

    def calculate_subtotal(self) -> float:
        return sum(item.calculate_item_total() for item in self.items)

    def calculate_tax(self) -> float:
        return (self.calculate_subtotal() * self.tax_rate_percent) / 100.0

    def calculate_grand_total(self) -> float:
        return self.calculate_subtotal() + self.calculate_tax()

    def generate_receipt(self):
        if not self.items:
            print("Bill is empty. No items added.")
            return

        print("\n" + "=" * 52)
        print(f"{'INVOICE / RECEIPT':^52}")
        print("=" * 52)
        print(f"Customer Name : {self.customer_name}")
        print(f"Date & Time   : {self.date_time}")
        print("-" * 52)
        print(f"{'Item':<20} | {'Qty':<5} | {'Price ($)':<10} | {'Total ($)':<10}")
        print("-" * 52)

        for item in self.items:
            item_total = item.calculate_item_total()
            print(f"{item.name:<20} | {item.quantity:<5} | {item.price:<10.2f} | {item_total:<10.2f}")

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        grand_total = self.calculate_grand_total()

        print("-" * 52)
        print(f"{'Subtotal:':<40} ${subtotal:>9.2f}")
        print(f"{f'Tax ({self.tax_rate_percent}%):':<40} ${tax:>9.2f}")
        print("=" * 52)
        print(f"{'GRAND TOTAL:':<40} ${grand_total:>9.2f}")
        print("=" * 52)
        print(f"{'Thank you for your business!':^52}\n")


def main():
    print("=== OOP BILLING SYSTEM ===")
    customer = input("Enter Customer Name: ").strip() or "Valued Customer"
    bill = Bill(customer_name=customer, tax_rate_percent=5.0)

    while True:
        print("\n1. Add Item to Bill")
        print("2. Generate & View Final Bill")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Price per unit ($): "))
                quantity = int(input("Enter Quantity: "))
                
                if price < 0 or quantity <= 0:
                    print("Price must be >= 0 and quantity must be at least 1.")
                    continue
                    
                product = Product(name, price, quantity)
                bill.add_product(product)
                print(f"Added {quantity} x '{name}' to bill.")
            except ValueError:
                print("Error: Invalid price or quantity format!")

        elif choice == '2':
            bill.generate_receipt()
            break
        elif choice == '3':
            print("Exiting Billing System.")
            break
        else:
            print("Invalid choice! Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()