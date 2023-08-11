#######################
from itertools import product 
import numpy as np 
with open('rosalind_ba1k.txt','r') as f:
    seq = f.readline().strip()
    info = f.readline().strip()
    info = int(info)
    
    
a = list(product('ACGT',repeat=info))
all_poss1 = []
index2 = []
frequency3 = []
for i in a:
    b = ''.join(i)
    all_poss1.append(b)

for i in range(4**info):
    index2.append(i)

for j in all_poss1:
    count = 0
    for i in range(len(seq)-info+1):
        seq_particle = seq[i:i+info]
        if j == seq_particle:
            count += 1 
    frequency3.append(count)
for i in frequency3:
    print(i,end=' ')

