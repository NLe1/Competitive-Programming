n = int(input())

line = []
for x in range(n):
    line.append(input())

if sorted(line, reverse=True) == line:
    print("DECREASING")
elif sorted(line) == line:
    print("INCREASING")
else:
    print("NEITHER")