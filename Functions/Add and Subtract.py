def sum_numbers(num1, num2):
    return num1 + num2


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    subtraction_result = subtract(result, num3)
    return subtraction_result


num1 = int(input())
num2 = int(input())
num3 = int(input())


result = add_and_subtract(num1, num2, num3)
print(result)
