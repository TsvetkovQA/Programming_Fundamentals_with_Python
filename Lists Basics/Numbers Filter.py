n = int(input())

integers = []

for _ in range(n):
    number = int(input())
    integers.append(number)

command = input()

if command == "even":
    result = [num for num in integers if num % 2 == 0]
elif command == "odd":
    result = [num for num in integers if num % 2 != 0]
elif command == "negative":
    result = [num for num in integers if num < 0]
elif command == "positive":
    result = [num for num in integers if num >= 0]

print(result)
