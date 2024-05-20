from domain.product import Product
from repository.databaseConnection import DatabaseConnection


class RepositoryWerehouse:
    repositoryWerehouse = DatabaseConnection()

    def create_product(self, product: Product):
        global cursor, connection
        try:
            query = """INSERT INTO products (name, description, price, quantity) VALUES
            (%s, %s, %s, %s) RETURNING *"""
            params = (product.name, product.description, product.price, product.quantity)
            connection, cursor = self.repositoryWerehouse.execute_query(query, params)
            result = cursor.fetchone()
            connection.commit()
            return result
        except Exception as e:
            print(f"An unexpected error occurred while creating product: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_product_by_name(self, name: str):
        query = f"Select * from products where name = '{name}'"
        return self.repositoryWerehouse.fetch_data(query)

    def get_products(self):
        query = f"Select * from products"
        return self.repositoryWerehouse.fetch_data(query)

    def delete_product(self, name: str):
        try:
            query = "DELETE FROM products WHERE name = %s"
            params = (name,)
            connection, cursor = self.repositoryWerehouse.execute_query(query, params)
            connection.commit()
            return True
        except Exception as e:
            print(f"An unexpected error occurred while deleting product: {e}")
            return False


    def update_product(self, name: str, updated_product: Product):
        global cursor, connection
        try:
            current_product_query = "SELECT description, price, quantity FROM products WHERE name = %s"
            connection, cursor = self.repositoryWerehouse.execute_query(current_product_query, (name,))
            current_product = cursor.fetchone()

            updated_description = updated_product.description if updated_product.description is not None else current_product[0]
            updated_price = updated_product.price if updated_product.price is not None else current_product[1]
            update_quantity = updated_product.quantity if updated_product.quantity is not None else current_product[2]

            query = """
            UPDATE products SET
                description = %s,
                price = %s,
                quantity = %s
            WHERE name = %s RETURNING *"""
            params = (updated_description, updated_price, update_quantity, name)
            connection, cursor = self.repositoryWerehouse.execute_query(query, params)
            result = cursor.fetchone()
            connection.commit()
            return result
        except Exception as e:
            print(f"An unexpected error occurred while updating product: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def update_stock(self, name: str, quantity: int):
        global cursor, connection
        try:
            query = """
            UPDATE products
            SET quantity = quantity + %s
            WHERE name = %s
            RETURNING *
            """

            params = (quantity, name)
            connection, cursor = self.repositoryWerehouse.execute_query(query, params)
            result = cursor.fetchone()
            connection.commit()
            return result
        except Exception as e:
            print(f"An unexpected error occurred while updating stock: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def calcul_product_statistics(self):
        global cursor, connection
        try:
            query = """
            SELECT COUNT(*) AS product_count,
                   AVG(price) AS average_price,
                   SUM(quantity) AS total_quantity
            FROM products
            """
            connection, cursor = self.repositoryWerehouse.execute_query(query, params=None)
            statistic = cursor.fetchone()
            return statistic
        except Exception as e:
            print(f"An unexpected error occurred while calculating product statistics: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()