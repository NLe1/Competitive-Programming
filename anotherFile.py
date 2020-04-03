import itertools
c = "AAPPAPAAABAA"
for k, g in itertools.groupby(c):
    print(k,len(list(g)))