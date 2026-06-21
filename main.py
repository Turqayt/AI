import sqlite3

def setup_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')

setup_database()


class InventoryManager:
    def __init__(self):
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, quantity, price):
        self.cursor.execute('''
            INSERT INTO products (name, quantity, price)
            VALUES (?, ?, ?);
        ''', (name, quantity, price))
        self.conn.commit()

    def view_inventory(self):
        self.cursor.execute('''
            SELECT * 
            FROM products
        ''')
        items = self.cursor.fetchall()
        for item in items:
            print(item)


def main_menu():
    # Instantiate our OOP class
    manager = InventoryManager()

    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add a Product")
        print("2. View Inventory")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            manager.add_product(name, quantity, price)
            print(f"{name} added successfully!")

        elif choice == '2':
            manager.view_inventory()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

main_menu()