def is_palindrome(some_num: str) -> bool:
    if some_num == some_num[::-1]:
        return True
    return False


numbers = input().split(", ")
for current_number in numbers:
    print(is_palindrome(current_number))
