from Bio import SeqIO
import math
with open('rosalind_mmch.txt','r') as f:
    raw = SeqIO.read(f,'fasta')
    seq = str(raw.seq)
A_count = seq.count('A')
C_count = seq.count('C')
G_count = seq.count('G')
U_count = seq.count('U')

def factorial(count1,count2):
    if count1 == count2:
        return math.factorial(count1)//math.factorial(count1-count2)
    elif count1 < count2:
        return math.factorial(count2)//math.factorial(count2-count1)
    else:
        return math.factorial(count1)//math.factorial(count1-count2)
    return
print(int(factorial(A_count,U_count)*factorial(C_count,G_count)))


# from Bio import SeqIO
# from math import factorial
# sequence = ''
# with open('rosalind_mmch.txt', 'r') as f:
#     for record in SeqIO.parse(f, 'fasta'):
#         sequence = str(record.seq)

# A, U, G, C = 0, 0, 0, 0
# for nt in sequence:
#     if nt == 'A':
#         A += 1
#     elif nt == 'U':
#         U += 1
#     elif nt == 'G':
#         G += 1
#     elif nt == 'C':
#         C += 1

# AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
# GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
# print(int(AU * GC))