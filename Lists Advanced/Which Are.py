first_sequence = input().split(", ")
second_sequence = input().split(", ")

result = []

for string1 in first_sequence:
    if any(string1 in string2 for string2 in second_sequence):
        result.append(string1)

print(result)
