words = input().split()
even_words = [word for word in words if len(word) % 2 == 0]
result = '\n'.join(even_words)
print(result)
