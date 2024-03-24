command = input()

current_seats = 0
total_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0

while command != "Finish":
    movie_name = command
    taken_seats = 0
    available_seats = int(input())
    type_of_ticket = input()

    while type_of_ticket != "End":
        total_tickets += 1
        taken_seats += 1

        if type_of_ticket == "student":
            student_count += 1
        elif type_of_ticket == "standard":
            standard_count += 1
        elif type_of_ticket == "kid":
            kid_count += 1

        if available_seats == taken_seats:
            break

        type_of_ticket = input()

    percent_occupancy = taken_seats / available_seats * 100
    print(f"{movie_name} - {percent_occupancy :.2f}% full.")

    command = input()

percent_of_total_tickets = total_tickets / available_seats * 100
percent_of_student_tickets = student_count / total_tickets * 100
percent_of_standard_tickets = standard_count / total_tickets * 100
percent_of_kid_tickets = kid_count / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_of_student_tickets :.2f}% student tickets.")
print(f"{percent_of_standard_tickets :.2f}% standard tickets.")
print(f"{percent_of_kid_tickets :.2f}% kids tickets.")
