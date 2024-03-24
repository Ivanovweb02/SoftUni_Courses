force = input()
force_book = {}
while force != 'Lumpawaroo':
    if '|' in force:
        force_side, force_user = force.split(" | ")
        is_user_in_side = False
        for value in force_book.values():
            if force_user in value:
                is_user_in_side = True
                break
        if not is_user_in_side:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif '->' in force:
        force_user, force_side = force.split(" -> ")
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    force = input()

for (side, user) in force_book.items():
    if len(user) > 0:
        print(f"Side: {side}, Members: {len(user)}")
        print('!', '\n! '.join(user))
