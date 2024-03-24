def sorting_num(list_of_num):
    positive_nums = [x for x in list_of_num if x > 0]
    negative_nums = [y for y in list_of_num if y < 0]

    def negative_nums_sum():
        return sum(negative_nums)

    def positive_nums_sum():
        return sum(positive_nums)

    print(f"{negative_nums_sum()}\n{positive_nums_sum()}")

    if abs(positive_nums_sum()) > abs(negative_nums_sum()):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


some_numbers = [int(x) for x in input().split()]
sorting_num(some_numbers)
