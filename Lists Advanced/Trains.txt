num_wagons = int(input())
train = [0] * num_wagons

while True:
    command = input().split()

    if command[0] == "End":
        break

    action, *args = command

    if action == "add":
        people = int(args[0])
        train[-1] += people
    elif action == "insert":
        index, people = int(args[0]), int(args[1])
        train[index] += people
    elif action == "leave":
        index, people = int(args[0]), int(args[1])
        train[index] -= people

print(train)
