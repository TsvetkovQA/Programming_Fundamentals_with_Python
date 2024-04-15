input_str = input()

numbers_str = input_str.split()

opposite_numbers = []

for num_str in numbers_str:
    try:
        num = int(num_str)
        opposite_numbers.append(-num)
    except ValueError:
        print(f"Skipping invalid input: {num_str}")

print(opposite_numbers)
