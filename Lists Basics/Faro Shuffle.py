initial_deck_str = input()
faro_shuffles = int(input())

deck = initial_deck_str.split()

for _ in range(faro_shuffles):
    half_size = len(deck) // 2
    shuffled_deck = []

    for i in range(half_size):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[i + half_size])

    deck = shuffled_deck

print(deck)
