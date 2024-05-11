numbers = input().split(", ")
even_indices = [str(i) for i, num in enumerate(numbers) if int(num) % 2 == 0]

print('[' + ', '.join(even_indices) + ']')
