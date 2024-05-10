def perform_operation(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


input_operator = input()
first_num = int(input())
second_num = int(input())


result = perform_operation(input_operator, first_num, second_num)


print(result)
