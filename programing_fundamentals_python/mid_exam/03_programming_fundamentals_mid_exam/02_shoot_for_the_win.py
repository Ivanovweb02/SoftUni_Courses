target_values = list(map(int, input().split()))
command = input()
count = 0

while command != 'End':
    index = int(command)
    if index in range(len(target_values)):
        if target_values[index] != -1:
            count += 1
            shut_target = target_values[index]
            target_values[index] = -1
            for digit in range(len(target_values)):
                if target_values[digit] != -1:
                    if target_values[digit] > shut_target:
                        target_values[digit] -= shut_target
                    else:
                        target_values[digit] += shut_target

    command = input()

result = ' '.join(map(str, target_values))
print(f"Shot targets: {count} -> {result}")
