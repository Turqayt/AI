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

    def update_quantity(self, product_id, new_quantity):
        self.cursor.execute('''
            UPDATE products 
            SET quantity = ?
            WHERE id = ?;
        ''', (new_quantity, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products WHERE id = ?;
        ''', (product_id,))


def main_menu():
    # Instantiate our OOP class
    manager = InventoryManager()

    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add a Product")
        print("2. View Inventory")
        print("3. Exit")
        print("4. Update Quantity")
        print("5. Delete Product")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                manager.add_product(name, quantity, price)
                print(f"{name} added successfully!")
            except ValueError:
                print("Error: Quantity must be a whole number, and price must be a number.")

        elif choice == '2':
            manager.view_inventory()

        elif choice == '3':
            print("Goodbye!")
            break

        elif choice == '4':
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            manager.update_quantity(product_id, quantity)

        elif choice == '5':
            product_id = int(input("Enter product ID: "))
            manager.delete_product(product_id)

        else:
            print("Invalid choice, please try again.")

main_menu()