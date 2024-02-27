n = int(input())

for i in range(1, n + 1):
    stars = "*" * i
    print(stars)

for i in range(n - 1, 0, -1):
    stars = "*" * i
    print(stars)
