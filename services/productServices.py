from repository.repositoryWerehouse import RepositoryWerehouse
from services.mapper import map_products,map_product_statistics
from domain.product import Product

class ProductServices:
    repo_product = RepositoryWerehouse()

    def get_products(self):
        raw_data = self.repo_product.get_products()
        return map_products(raw_data)

    def get_product_by_name(self, name: str):
        raw_data = self.repo_product.get_product_by_name(name)
        return map_products(raw_data)

    def get_product_statistic(self):
        statistic = self.repo_product.calcul_product_statistics()
        return map_product_statistics(statistic)

    def create_product(self, product: Product):
        create_product = self.repo_product.create_product(product)
        return map_products([create_product])

    def delete_product(self, name: str):
        try:
            return self.repo_product.delete_product(name)
        except Exception as e:
            print(f"An unexpected error occurred while deleting product: {e}")
            return False

    def update_product(self, name: str, updated_product: Product):
        upd_product = self.repo_product.update_product(name, updated_product)
        return map_products([upd_product])

    def manage_stock(self, name: str, action: str, quantity: int):
        if action == "increase":
            increase_product = self.repo_product.update_stock(name, quantity)
            return map_products([increase_product])
        elif action == "decrease":
            decrease_product = self.repo_product.update_stock(name, -quantity)
            return map_products([decrease_product])
        else:
            raise ValueError("Invalid action. Must be 'increase' or 'decrease'")


