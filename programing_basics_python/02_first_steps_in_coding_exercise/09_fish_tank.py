# 1.	Дължина в см – цяло число в интервала [10 … 500]
# 2.	Широчина в см – цяло число в интервала [10 … 300]
# 3.	Височина в см – цяло число в интервала [10… 200]
# 4.	Процент  – реално число в интервала [0.000 … 100.000]

length_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percent = float(input()) * 0.01

aquarium_volume = length_in_centimeters \
                  * width_in_centimeters \
                  * height_in_centimeters

volume_in_liter = aquarium_volume * 0.001

occupied_space = percent

needed_liters = volume_in_liter * (1 - occupied_space)

print(needed_liters)

