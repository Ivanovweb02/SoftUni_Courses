count = int(input())

synonyms = {}

for _ in range(count):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for (key, value) in synonyms.items():
    synonym_string = ', '.join(value)
    print(f"{key} - {synonym_string}")
