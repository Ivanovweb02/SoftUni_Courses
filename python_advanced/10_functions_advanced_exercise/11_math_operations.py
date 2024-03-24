def math_operations(*nums, **kwargs):
    keys = list(kwargs)

    for i in range(len(nums)):
        key = keys[i % 4]
        if key == 'a':
            kwargs[key] += nums[i]
        elif key == 's':
            kwargs[key] -= nums[i]
        elif key == 'd':
            if nums[i] != 0:
                kwargs[key] /= nums[i]
        elif key == 'm':
            kwargs[key] *= nums[i]

    result = ''

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f"{key}: {value :.1f}\n"

    return result


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
