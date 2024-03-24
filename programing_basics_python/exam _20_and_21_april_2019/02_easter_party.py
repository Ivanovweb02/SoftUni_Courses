count_guest = int(input())
price_per_envelope_per_person = float(input())
budget = float(input())

discount = 0

if 10 <= count_guest <= 15:
    discount = price_per_envelope_per_person * 0.15
elif 15 < count_guest <= 20:
    discount = price_per_envelope_per_person * 0.20
elif count_guest > 20:
    discount = price_per_envelope_per_person * 0.25

cake = budget * 0.10

total_cost = cake + count_guest * (price_per_envelope_per_person - discount)
if budget >= total_cost:
    left_amount = budget - total_cost
    print(f"It is party time! {left_amount :.2f} leva left.")
else:
    needed_amount = total_cost - budget
    print(f"No party! {needed_amount :.2f} leva needed.")
