import math
with open('rosalind_pper.txt','r') as f:
    for line in f:
        info = line.strip().split()
        n = int(info[0])
        k = int(info[1])
def permutation(n,k):
    return int((math.factorial(n)/math.factorial(n-k))%1000000)
print(permutation(n,k))