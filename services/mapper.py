from domain.product import Product

def map_products(data: list):
    products = []
    for row in data:
        product = Product(
            name=row[1],
            description=row[2],
            price=row[3],
            quantity=row[4]
        )
        products.append(product)
    return products

def map_product_statistics(statistic):
    if statistic:
        return {
            "product_count": statistic[0],
            "average_price": statistic[1],
            "total_quantity": statistic[2]
        }
    else:
        return None
