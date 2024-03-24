def even_odd_filter(**kwargs):
    sorted_dict = {}
    for name, value in sorted(kwargs.items(), key=lambda x: -len(x[1])):
        if name == 'odd':
            kwargs[name] = [x for x in value if x % 2 != 0]
        elif name == 'even':
            kwargs[name] = [y for y in value if y % 2 == 0]

        sorted_dict[name] = kwargs[name]
    return sorted_dict


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
