

def valid_ticket(some_ticket):
    winning_symbols = ['@', '#', '$', '^']
    if len(some_ticket) == 20:
        left_part = some_ticket[:10]
        right_part = some_ticket[10:]
        for symbol in winning_symbols:
            if symbol in left_part and symbol in right_part:
                for count in range(10, 5, -1):
                    winning_count_of_symbols = symbol * count
                    if winning_count_of_symbols in left_part \
                            and winning_count_of_symbols in right_part:
                        if len(winning_count_of_symbols) == 10:
                            return f"ticket \"{ticket}\" - {len(winning_count_of_symbols)}{symbol} Jackpot!"
                        return f"ticket \"{ticket}\" - {len(winning_count_of_symbols)}{symbol}"
        return f"ticket \"{ticket}\" - no match"
    return "invalid ticket"


tickets = [ticket.strip() for ticket in input().split(', ')]

for ticket in tickets:
    print(valid_ticket(ticket))
