import sqlite3
from definition import PROJECT_ROOT


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(PROJECT_ROOT / 'become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self) -> None:
        """Check the connection to the database"""

        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self) -> list:
        """Get a list of all users"""

        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_user_address_by_name(self, name: str) -> list:
        """
        Get a user address by name
        :param name: set user address
        """

        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def update_product_qnt_by_id(self, product_id: int, qnt: int) -> None:
        """
        Update product quantity  by id
        :param product_id: set product id
        :param qnt: set quantity
        """

        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id: int) -> list:
        """
        Select product quantity by id
        :param product_id: set product id
        """

        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def insert_product(self, product_id: int, name: str, description: str, qnt: int) -> None:
        """
        Insert a product into database
        :param product_id: set product id
        :param name: set product name
        :param description: set product description
        :param qnt: set quantity
        """

        query = f"INSERT INTO products (id, name, description, quantity) " \
                f"VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id: int) -> None:
        """
        Delete product from database by id
        :param product_id: set product id
        """
        query = f"DELETE FROM products WHERE id = '{product_id}'"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self) -> list:
        """Get detailed orders from database"""

        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date" \
                " FROM orders" \
                " JOIN customers ON orders.customer_id = customers.id" \
                " JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
