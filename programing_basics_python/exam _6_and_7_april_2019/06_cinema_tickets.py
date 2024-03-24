command = input()


total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while command != "Finish":
    movie_name = command
    taken_seat = 0
    available_seats = int(input())
    ticket_type = input()

    while ticket_type != "End":
        taken_seat += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        if taken_seat == available_seats:
            break
        ticket_type = input()
    percent_full = (taken_seat / available_seats) * 100
    print(f"{movie_name} - {percent_full :.2f}% full.")
    command = input()

percent_student = (student_tickets / total_tickets) * 100
percent_standard = (standard_tickets / total_tickets) * 100
percent_kid = (kids_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student :.2f}% student tickets.")
print(f"{percent_standard :.2f}% standard tickets.")
print(f"{percent_kid :.2f}% kids tickets.")
