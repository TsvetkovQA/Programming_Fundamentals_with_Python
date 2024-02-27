n = int(input())

odd_found = False

for _ in range(n):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        odd_found = True
        break

if not odd_found:
    print("All numbers are even.")
