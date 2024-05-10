numbers = list(map(int, input().split(', ')))

group_boundary = 10
max_group = max(numbers)

while group_boundary <= max_group:
    current_group = [num for num in numbers if group_boundary - 10 < num <= group_boundary]
    if current_group:
        print(f"Group of {group_boundary}'s: {current_group}")
    else:
        print(f"Group of {group_boundary}'s: []")
    group_boundary += 10
    numbers = [num for num in numbers if num not in current_group]

if numbers:
    print(f"Group of {group_boundary}'s: {numbers}")
