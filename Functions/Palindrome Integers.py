def is_palindrome(number):

    number_str = str(number)


    return number_str == number_str[::-1]



input_list = input().split(", ")


input_numbers = [int(x) for x in input_list]


for number in input_numbers:
    result = is_palindrome(number)
    print(result)
