bitcoins_count = int(input())
chinese_yuan_count = float(input())
commission = float(input())

bitcoin_to_euro = (bitcoins_count * 1168) / 1.95
yuan_to_euro = ((chinese_yuan_count * 0.15) * 1.76) / 1.95
total_euro = bitcoin_to_euro + yuan_to_euro
total_euro -= total_euro * (commission / 100)

print(f"{total_euro :.2f}")
