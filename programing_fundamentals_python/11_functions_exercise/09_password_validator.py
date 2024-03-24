def valid_password(password: str) -> list:
    errors = []
    if len(password) < 6 or len(password) > 10:
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for character in password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        errors.append("Password must have at least 2 digits")
    return errors


password_input = input()
validated_password = valid_password(password_input)
if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))
