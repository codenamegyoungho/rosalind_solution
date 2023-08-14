from itertools import product 
base = ['A','B','C','D','E','F','G','H','I']
a = list(product(base,repeat=3))
b = []
for i in a:
    b.append(''.join(i))

for i in b:
    print(i)