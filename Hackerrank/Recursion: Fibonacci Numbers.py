def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    prev, cur, counter = 1, 1, 2
    while counter < n:
        temp = prev
        prev = cur
        cur = cur + temp
        counter += 1
    return cur

n = int(input())
print(fibonacci(n))