first, second = input().split()
total_sum = 0


if len(first) == len(second):
    for index in range(len(first)):
        first_char = ord(first[index])
        second_char = ord(second[index])
        total_sum += first_char * second_char

elif len(first) > len(second):
    for index in range(len(second)):
        first_char = ord(first[index])
        second_char = ord(second[index])
        total_sum += first_char * second_char
    diff = len(first) - len(second)
    for index in range(len(first) - diff, len(first)):
        first_char = ord(first[index])
        total_sum += first_char

else:
    for index in range(len(first)):
        first_char = ord(first[index])
        second_char = ord(second[index])
        total_sum += first_char * second_char
    diff = len(second) - len(first)
    for index in range(len(second) - diff, len(second)):
        second_char = ord(second[index])
        total_sum += second_char

print(total_sum)
