count = int(input())

odd_collection = set()
even_collection = set()
result = set()

for row in range(1, count + 1):
    name = input()
    ascii_sum = sum([ord(char) for char in name])
    ascii_sum /= row
    ascii_sum = int(ascii_sum)
    if ascii_sum % 2 == 0:
        even_collection.add(ascii_sum)
    else:
        odd_collection.add(ascii_sum)

if sum(odd_collection) == sum(even_collection):
    result = odd_collection | even_collection

elif sum(odd_collection) > sum(even_collection):
    result = odd_collection - even_collection

elif sum(odd_collection) < sum(even_collection):
    result = odd_collection ^ even_collection

result = [str(num) for num in result]
print(', '.join(result))
