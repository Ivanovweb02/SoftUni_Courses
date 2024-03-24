count = int(input())
collection = set()

for _ in range(count):
    username = input()
    collection.add(username)

print('\n'.join(collection))
