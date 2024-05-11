def calculate_order_price(product, quantity):
    product_prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }

    if product in product_prices:
        price_per_item = product_prices[product]
        total_price = price_per_item * quantity
        return total_price
    else:
        return "Invalid product"

product = input()
quantity = int(input())

result = calculate_order_price(product, quantity)

print(f"{result:.2f}")
