words = input().split()
palindrome = input()
list_of_palindrome = [word for word in words if word == word[::-1]]
count_of_palindrome = list_of_palindrome.count(palindrome)

print(f"{list_of_palindrome}\nFound palindrome {count_of_palindrome} times")
