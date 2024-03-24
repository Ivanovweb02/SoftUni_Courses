company_name = input()
adult_tickets_count = int(input())
kid_tickets_count = int(input())
net_price_per_adult_ticket = float(input())
service_price = float(input())

net_price_per_kid_ticket = net_price_per_adult_ticket * (1 - 0.70)

total_price = adult_tickets_count * (net_price_per_adult_ticket + service_price) \
              + kid_tickets_count * (net_price_per_kid_ticket + service_price)

agency_profit = total_price * 0.20
print(f"The profit of your agency from {company_name} tickets is {agency_profit :.2f} lv.")
