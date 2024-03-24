first_length, second_length = list(map(int, input().split()))
first_collection = []
second_collection = []

while len(second_collection) != second_length:
    number = int(input())
    if len(first_collection) < first_length:
        first_collection.append(number)
    else:
        second_collection.append(number)

first_collection = set(first_collection)
second_collection = set(second_collection)
intersection = first_collection & second_collection
for num in intersection:
    print(num)
