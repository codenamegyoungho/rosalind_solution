import math
with open('rosalind_lia (2).txt','r') as f:
    info = f.readline().strip().split()
    info = [int(i) for i in info]
sum = 0
지수 = 2**info[0]

for i in range(info[1]):
    sum += math.comb(지수,i)*((3/4)**(지수-i))*((1/4)**i)
print(1-sum)