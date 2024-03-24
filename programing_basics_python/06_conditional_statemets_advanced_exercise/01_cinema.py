projection = input()
number_of_rows = int(input())
number_of_columns = int(input())

projection_price = 0

if projection == "Premiere":
    projection_price = 12.00
elif projection == "Normal":
    projection_price = 7.50
elif projection == "Discount":
    projection_price = 5.00

total_income = projection_price * number_of_rows * number_of_columns
print(f"{total_income:.2f} leva")
