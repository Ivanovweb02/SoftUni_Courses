volume_of_pool = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

quantity_per_hour_1 = pipe_1 * hours
quantity_per_hour_2 = pipe_2 * hours
litters_more = 0
total_quantity = quantity_per_hour_1 + quantity_per_hour_2
percent_of_full = total_quantity / volume_of_pool * 100
percent_of_pipe_1 = quantity_per_hour_1 / total_quantity * 100
percent_of_pipe_2 = quantity_per_hour_2 / total_quantity * 100

if volume_of_pool < total_quantity:
    litters_more += total_quantity - volume_of_pool
    print(f"For {hours:.2f} hours the pool overflows with {litters_more:.2f} liters.")

else:
    print(f"The pool is {percent_of_full:.2f}% full. Pipe 1: \
{percent_of_pipe_1:.2f}%. Pipe 2: {percent_of_pipe_2:.2f}%.")
