factor = int(input())
count = int(input())

multiples = []

for i in range(count):
    multiple = factor * (i + 1)
    multiples.append(multiple)

print(multiples)
