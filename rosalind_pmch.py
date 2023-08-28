from itertools import permutations
import math
def count_base(seq,base):
    countings = []
    for char in base:
        count_char = seq.count(char)
        countings.append(count_char)
    return countings

with open('rosalind_pmch.txt','r') as f:
    for line in f:
        if line.startswith('>'):
            continue
        else:
            seq = line.strip()
            break
count_base_result = count_base(seq,'ACGU')
a = math.perm(count_base_result[0],count_base_result[0])
c = math.perm(count_base_result[1],count_base_result[1])    
print(a*c)
