contact_info = input()
dictionary = {}

while '-' in contact_info:

    name, number = contact_info.split('-')
    dictionary[name] = number

    contact_info = input()

time_of_search = int(contact_info)
for _ in range(time_of_search):
    search_name = input()
    if search_name in dictionary:
        print(f"{search_name} -> {dictionary[search_name]} ")
    else:
        print(f"Contact {search_name} does not exist.")
