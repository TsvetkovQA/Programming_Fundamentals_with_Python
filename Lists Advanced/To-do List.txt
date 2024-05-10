to_do_notes = []

while True:
    command = input()

    if command == "End":
        break

    importance, note = command.split("-")
    importance = int(importance)

    to_do_notes.append((importance, note))

to_do_notes.sort(key=lambda x: x[0])
result = [note for importance, note in to_do_notes]

print(result)
