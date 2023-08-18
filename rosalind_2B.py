import re
from itertools import product
from Bio.Seq import Seq 
from Bio import motifs 
base = ['A','C','G','T']
pattern = list(product(base,repeat=6))
patterns = [''.join(i) for i in pattern]

testing = re.compile('[a-zA-Z]')
seqs = []
with open('rosalind_ba2b.txt','r') as f:
    for line in f:
        if testing.match(line):
            seqs.append(line.strip())
        else:
            info = line.strip().split()
int_info = [int(i) for i in info]

def hamming_distance(patterns, seqs):
    answer = {}
    for pattern in patterns:
        result_min = int_info[0]
        for seq in seqs:
            for j in range(len(seq) - int_info[0] + 1):
                seq_particle = seq[j:j + int_info[0]]
                count = sum(1 for p, s in zip(pattern, seq_particle) if p != s)
                result_min = min(result_min, count)
                count = 0
            answer[pattern] = answer.get(pattern, 0) + result_min  # 수정된 부분
            result_min = int_info[0]
    return answer
a = hamming_distance(patterns,seqs)
# def find_minimum_pattern(answer):
#     min_pattern = None
#     min_value = float('inf')
#     for pattern, value in answer.items():
#         if len(pattern) == int_info[0] and value < min_value:
#             min_pattern = pattern
#             min_value = value
#     return min_pattern
def find_minimum_pattern(answer):
    min_val = min(answer.values())
    min_pattern = []
    for i in answer:
        if answer[i] == min_val:
            min_pattern.append(i)
    return min_pattern
# 이 함수를 사용하여 최소 값을 가지는 3자리 패턴을 찾을 수 있습니다.
print('mimimumpattern',find_minimum_pattern(a))