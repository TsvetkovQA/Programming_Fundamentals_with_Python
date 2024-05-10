def is_perfect_number(number):
    divisors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sum(divisors) == number

number = int(input())

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
