employee_happiness = list(map(int, input().split()))

factor = int(input())

improved_happiness = [happiness * factor for happiness in employee_happiness]

average_happiness = sum(improved_happiness) / len(improved_happiness)

happy_count = sum(1 for happiness in improved_happiness if happiness >= average_happiness)
total_count = len(improved_happiness)


if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
