some_text = tuple(input())
unique_char = set([char for char in some_text])

for curr_char in sorted(unique_char):
    print(f"{curr_char}: {some_text.count(curr_char)} time/s")
