season = input()
group_type = input()
student_count = int(input())
night_count = int(input())

total_price = 0
discount = 0
type_of_sport = ""

if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        total_price = night_count * 9.60 * student_count
    elif season == "Spring":
        total_price = night_count * 7.20 * student_count
    elif season == "Summer":
        total_price = night_count * 15 * student_count

elif group_type == "mixed":
    if season == "Winter":
        total_price = night_count * 10.00 * student_count
    elif season == "Spring":
        total_price = night_count * 9.50 * student_count
    elif season == "Summer":
        total_price = night_count * 20 * student_count

if student_count >= 50:
    discount = total_price * 0.50
elif student_count >= 20:
    discount = total_price * 0.15
elif student_count >= 10:
    discount = total_price * 0.05

if group_type == "girls":
    if season == "Winter":
        type_of_sport = "Gymnastics"
    elif season == "Spring":
        type_of_sport = "Athletics"
    elif season == "Summer":
        type_of_sport = "Volleyball"

elif group_type == "boys":
    if season == "Winter":
        type_of_sport = "Judo"
    elif season == "Spring":
        type_of_sport = "Tennis"
    elif season == "Summer":
        type_of_sport = "Football"

elif group_type == "mixed":
    if season == "Winter":
        type_of_sport = "Ski"
    elif season == "Spring":
        type_of_sport = "Cycling"
    elif season == "Summer":
        type_of_sport = "Swimming"

total_price -= discount
print(f"{type_of_sport} {total_price :.2f} lv.")
