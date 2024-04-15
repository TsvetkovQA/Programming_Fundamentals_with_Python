items_input = input().split("|")
budget = float(input())


max_prices = {"Clothes": 50.00, "Shoes": 35.00, "Accessories": 20.50}


bought_items = []
profit = 0.0

for item_info in items_input:
    item_data = item_info.split("->")
    item_type, item_price = item_data[0], float(item_data[1])

    if item_type in max_prices and item_price <= max_prices[item_type] and budget >= item_price:
        budget -= item_price
        bought_items.append(item_price)
        profit += item_price * 0.4


bought_items = [item * 1.4 for item in bought_items]


print(" ".join([f"{item:.2f}" for item in bought_items]))


print(f"Profit: {profit:.2f}")


if budget + sum(bought_items) >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")
