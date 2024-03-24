number_1 = int(input())
number_2 = int(input())
print(f"Before:\na = {number_1}\nb = {number_2}")

number_1, number_2 = number_2, number_1
print(f"After: \na = {number_1}\nb = {number_2}")
