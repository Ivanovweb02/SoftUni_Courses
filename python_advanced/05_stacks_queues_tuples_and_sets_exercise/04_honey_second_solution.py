from collections import deque


def calculation(matched_bee, symbol, matched_nectar, honey):
    if symbol == '+':
        honey += matched_bee + matched_nectar
    elif symbol == '-':
        honey += abs(matched_bee - matched_nectar)
    elif symbol == '*':
        honey += abs(matched_bee * matched_nectar)
    elif symbol == '/':
        if matched_nectar != 0:
            honey += abs(matched_bee / matched_nectar)
    return honey


working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0
while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        total_honey = calculation(current_bee, current_symbol, current_nectar, total_honey)
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(bee) for bee in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(curr_nectar) for curr_nectar in nectar)}")
