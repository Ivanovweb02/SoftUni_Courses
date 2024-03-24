string = input()
string_1, string_2 = string.split()
total_sum = 0

for char_1, char_2 in zip(string_1, string_2):
    total_sum += ord(char_1) * ord(char_2)

if len(string_1) > len(string_2):
    total_sum += sum(ord(char) for char in string_1[len(string_2):])
elif len(string_2) > len(string_1):
    total_sum += sum(ord(char) for char in string_2[len(string_1):])

print(total_sum)
