count_easter_bread = int(input())
count_eggs = int(input())
cookies_kilograms = int(input())

easter_bread_price = count_easter_bread * 3.20
eggs_price = count_eggs * 4.35
cookies_price = cookies_kilograms * 5.40
egg_paint = count_eggs * 12 * 0.15

total_price = easter_bread_price + eggs_price + cookies_price + egg_paint
print(f"{total_price :.2f}")
