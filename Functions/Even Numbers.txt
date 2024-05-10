numbers = input().split()


numbers = list(map(int, numbers))


def is_even(num):
    return num % 2 == 0


even_numbers = list(filter(is_even, numbers))


print(even_numbers)
