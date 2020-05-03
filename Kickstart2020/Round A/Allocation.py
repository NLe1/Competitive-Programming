cases = int(input().rstrip())

for i in range(cases):
    line = input().rstrip().split()
    numHouses, budget = int(line[0]), int(line[1])
    prices = [int(item) for item in input().rstrip().split()]
    prices.sort()
    ct = 0
    for price in prices:
        if budget >= price:
            ct+=1
            budget-=price
        else:
            break
    print(f'Case #{i + 1}: {ct}')