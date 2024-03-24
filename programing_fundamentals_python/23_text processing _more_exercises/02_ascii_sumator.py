start = ord(input())
end = ord(input())
some_string = input()
sum_of_ascii = 0

for char in some_string:
    ascii_chart = ord(char)
    if start < ascii_chart < end:
        sum_of_ascii += ascii_chart
print(sum_of_ascii)
