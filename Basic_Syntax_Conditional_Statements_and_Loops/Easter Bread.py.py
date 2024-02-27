budget = float(input())
price_per_kg_flour = float(input())


price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_liter_milk = price_per_kg_flour * 1.25


loaves_count = 0
colored_eggs = 0

while budget >= price_per_kg_flour + price_per_pack_eggs + price_per_liter_milk / 4:
    loaves_count += 1
    colored_eggs += 3
    budget -= price_per_kg_flour + price_per_pack_eggs + price_per_liter_milk / 4

    if loaves_count % 3 == 0:
        colored_eggs -= loaves_count - 2


money_left = budget


print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
