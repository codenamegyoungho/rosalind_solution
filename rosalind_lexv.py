# import itertools
# n = 3
# alphabet = 'GUYJAMWSVDK'
# perm = []
# for i in range(1, n + 1):
#     perm.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))
# permutations = list(itertools.chain(*perm))
# srt_perm = sorted(permutations,
#                   key=lambda word: [alphabet.index(c) for c in word])
# with open('lexv_answer.txt', 'a') as f:
#     for j in srt_perm:
#         f.write('%s\n' % j)
from itertools import product 
import itertools
n = 3 
alphabet = 'DNA'
perm = []
for i in range(1, n + 1):
    perm.append(list(map(''.join,(product(alphabet, repeat=i)))))
permutations = list(itertools.chain(*perm))
srt_perm = sorted(permutations,
                  key=lambda word: [alphabet.index(c) for c in word])
with open('lexv_answer.txt', 'a') as f:
    for j in srt_perm:
        f.write(j + '\n')
