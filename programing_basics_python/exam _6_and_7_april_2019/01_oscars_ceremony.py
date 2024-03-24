hall_rent = int(input())

statuette = hall_rent * (1 - 0.30)
catering = statuette * (1 - 0.15)
voicing = catering * (1 - 0.50)

total_expenses = hall_rent + statuette + catering + voicing
print(f"{total_expenses :.2f}")
