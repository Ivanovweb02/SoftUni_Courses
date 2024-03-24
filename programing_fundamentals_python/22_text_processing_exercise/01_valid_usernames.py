list_of_usernames = input().split(", ")
valid_usernames = []

for username in list_of_usernames:
    if 3 <= len(username) <= 16 \
            and (username.isalnum() or '-' in username or '_' in username):
        print(username)
