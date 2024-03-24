def recursive_power(num, power):
    result = 0
    if power == 0:
        return 1

    result += num * recursive_power(num, power - 1)
    return result


print(recursive_power(2, 10))
