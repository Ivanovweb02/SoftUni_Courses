numbers_of_pens = int(input()) * 5.80
numbers_of_markers = int(input()) * 7.20
quantity_of_cleaning_product = int(input()) * 1.20
total_materials = numbers_of_pens + numbers_of_markers + quantity_of_cleaning_product
discount = int(input()) * 0.01 * total_materials
total_sum = numbers_of_markers + numbers_of_pens + quantity_of_cleaning_product - discount
print(total_sum)
