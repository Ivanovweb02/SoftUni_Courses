from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligent_value = int(input())
current_gun_barrel = size_of_the_gun_barrel

while bullets and locks:

    current_bullet = bullets.pop()
    current_gun_barrel -= 1
    intelligent_value -= bullet_price
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")
    if current_gun_barrel == 0:
        if bullets:
            if len(bullets) >= size_of_the_gun_barrel:
                current_gun_barrel += size_of_the_gun_barrel
            else:
                current_gun_barrel += len(bullets)
            print(f"Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligent_value}")
