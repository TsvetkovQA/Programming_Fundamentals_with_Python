gifts = input().split()
while True:
    command = input()
    if command == "No Money":
        break
    tokens = command.split()
    action = tokens[0]

    if action == "OutOfStock":
        gift_to_remove = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif action == "Required":
        gift_to_replace = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace

    elif action == "JustInCase":
        last_gift = tokens[1]
        gifts[-1] = last_gift

filtered_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(filtered_gifts))
