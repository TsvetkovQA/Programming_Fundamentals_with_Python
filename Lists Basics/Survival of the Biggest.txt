numbers_str = input()
n = int(input())

numbers = [int(num) for num in numbers_str.split()]

if n >= len(numbers):
    print()
else:

    for _ in range(n):
        numbers.remove(min(numbers))

    result_str = ", ".join(map(str, numbers))
    print(result_str)
