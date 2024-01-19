deck_of_cards = input().split(' ')
count_of_shuffles = int(input())
shuffled_deck = []

for _ in range(count_of_shuffles):
    shuffled_deck = []
    half_deck = len(deck_of_cards) // 2
    first_half = deck_of_cards[:half_deck]
    second_half = deck_of_cards[half_deck:]
    for current_index in range(len(first_half)):
        shuffled_deck.append(first_half[current_index])
        shuffled_deck.append(second_half[current_index])
    deck_of_cards = shuffled_deck

print(shuffled_deck)
