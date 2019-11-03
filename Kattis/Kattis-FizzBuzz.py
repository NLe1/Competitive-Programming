line = input()
line = line.split(" ")
x = int(line[0])
y = int(line[1])
n = int(line[2])

for i in range(1,n + 1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz", end="")
    elif i % x == 0:
        print("Fizz", end="")
    elif i % y == 0:
        print("Buzz", end="")
    else:
        print(i, end="")

    if i!=n:
        print()