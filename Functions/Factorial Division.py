def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num1 = int(input())
num2 = int(input())


factorial1 = factorial(num1)
factorial2 = factorial(num2)


division_result = factorial1 / factorial2


print(f"{division_result:.2f}")
