input_numbers = input()

numbers = [int(x) for x in input_numbers.split(', ')]

positive_numbers = [str(num) for num in numbers if num >= 0]
negative_numbers = [str(num) for num in numbers if num < 0]
even_numbers = [str(num) for num in numbers if num % 2 == 0]
odd_numbers = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}" if positive_numbers else "Positive:")
print(f"Negative: {', '.join(negative_numbers)}" if negative_numbers else "Negative:")
print(f"Even: {', '.join(even_numbers)}" if even_numbers else "Even:")
print(f"Odd: {', '.join(odd_numbers)}" if odd_numbers else "Odd:")
