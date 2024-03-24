from collections import deque

children = deque(input().split())
number = int(input()) - 1

while len(children) != 1:
    children.rotate(-number)
    removed_child = children.popleft()
    print(f"Removed {removed_child}")

print(f"Last is {children.pop()}")