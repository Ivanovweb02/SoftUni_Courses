city = input()
sell = float(input())
commission = 0

if city == "Sofia":
    if 0 <= sell <= 500:
        commission = sell * 0.05
    elif sell <= 1000:
        commission = sell * 0.07
    elif sell <= 10_000:
        commission = sell * 0.08
    elif sell > 10_000:
        commission = sell * 0.12

elif city == "Varna":
    if 0 <= sell <= 500:
        commission = sell * 0.045
    elif sell <= 1000:
        commission = sell * 0.075
    elif sell <= 10_000:
        commission = sell * 0.10
    elif sell > 10_000:
        commission = sell * 0.13

elif city == "Plovdiv":
    if 0 <= sell <= 500:
        commission = sell * 0.055
    elif sell <= 1000:
        commission = sell * 0.08
    elif sell <= 10_000:
        commission = sell * 0.12
    elif sell > 10_000:
        commission = sell * 0.145

if commission <= 0:
    print("error")

else:
    print(f"{commission:.2f}")
