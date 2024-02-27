budget = int(input())

total_spent = 0

overdraft = False

while True:
    product = input()

    if product == "End":
        break

    price = int(product)

    if total_spent + price > budget:
        overdraft = True
        break

    total_spent += price

if overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
