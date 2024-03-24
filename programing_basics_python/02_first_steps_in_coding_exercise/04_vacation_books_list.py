total_pages = int(input())
pages_per_hour = int(input())
days = int(input())
total_time = total_pages // pages_per_hour
needed_hours_in_a_day = total_time / days
print(needed_hours_in_a_day)
