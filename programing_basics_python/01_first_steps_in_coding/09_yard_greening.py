# а един кв. м. е 7.61 лв със ДД
# 18% отстъпка от крайната цена.

price_for_square_meter = 7.61
greened_square_meters = float(input())
total_sum = greened_square_meters * price_for_square_meter
discount = total_sum * 0.18

final_price = total_sum - discount

print(f'The final price is {final_price} lv.')
print(f'The discount is {discount} lv.')


