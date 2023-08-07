# from Bio.Seq import Seq 


# def find(target,hamming):
#     result = []
#     base = ['A','C','G','T']
    

#     def ca(remain_distance,current_seq,index):
#         remain = remain_distance
#         if remain == 0:
#             result.append(current_seq)
#             return 

#         for u in range(index,len(current_seq)):
#             for char in base:
#                 if current_seq[u] != char:
#                     new_seq = current_seq[:u] + char + current_seq[u+1:]
#                     ca(remain_distance-1,new_seq,u+1)
#     ca(hamming,target,0)
#     return result




# with open('rosalind_ba1j (1).txt','r') as f:
#     seq = f.readline().strip()
#     info = f.readline().strip().split()
#     info = [int(i) for i in info]
# fivethree = []

# neighbors = []
# rev_neighbors = []
# neighbors_di = {}
# rev_neighbors_di = {}
# for i in range(len(seq)-info[0]+1):
#     particle = Seq(seq[i:i+info[0]])
#     fivethree.append(particle)
# for part in fivethree:
#     for number in range(info[1]+1):
#         a = find(part,number)
#         for s in a:
#             neighbors.append(s)
# for i in neighbors:
#     # rev_neighbors.append(i[::-1])
#     i = Seq(i)
#     rev_neighbors.append(i.reverse_complement())


# ##fivethree neighbors is just easy way! 
# for i in neighbors:
#     gaesoo = 0
#     for s in fivethree:
#         count = 0
#         for u in range(info[0]):
#             if i[u] != s[u]:
#                 count += 1
#         if count <= info[1]:
#             gaesoo += 1               
#     neighbors_di[i] = gaesoo


# for i in rev_neighbors:
#     gaesoo = 0
#     for s in fivethree:
#         count = 0
#         for u in range(info[0]):
#             if i[u] != s[u]:
#                 count += 1
#         if count <= info[1]:
#             gaesoo += 1               
#     rev_neighbors_di[i] = gaesoo
# sum_list = []
# for kone,ktwo in zip(neighbors_di.keys(),rev_neighbors_di.keys()):
#     sum = 0
#     sum = neighbors_di[kone]+rev_neighbors_di[ktwo] 
#     sum_list.append(sum)

# for kone,ktwo in zip(neighbors_di.keys(),rev_neighbors_di.keys()):
#     if neighbors_di[kone]+rev_neighbors_di[ktwo] == max(sum_list):
#         print(kone,end= ' ') 


# max_number = []



# ^_^ coding:utf-8 ^_^

"""
Find Frequent Words with Mismatches and Reverse Complements
url: http://rosalind.info/problems/ba1j/

Given: A DNA string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
"""

from collections import defaultdict
from Bio import Seq

def HammingDistance(s1, s2):
    d = sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])
    return d

def ReversePattern(pattern):
    return Seq.reverse_complement(pattern)

def neighbour(pattern, mismatch, words):
    if mismatch == 0:
        words.add(pattern)
    else:
        bases = ['A', 'T', 'C', 'G']
        for i in range(len(pattern)):
            for j in range(len(bases)):
                new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
                if mismatch <= 1:
                    words.add(new_pattern)
                else:
                    neighbour(new_pattern, mismatch-1, words)

def FindMostFrequentPattern(text, k, d):
    allfrequentwords = defaultdict(int)
    for i in range(len(text) - k + 1):
        frequentwords = set()
        neighbour(text[i:i + k], d, frequentwords)

        for words in frequentwords:
            allfrequentwords[words] += 1

    for t in allfrequentwords.keys():
        reverse_k = ReversePattern(t)
        for i in range(len(text) - k + 1):
            if HammingDistance(text[i:i + k], reverse_k) <= d:
                allfrequentwords[t] += 1

    result = set()
    for t in allfrequentwords.keys():
        if allfrequentwords[t] == max(allfrequentwords.values()):
            result.add(t)
            result.add(ReversePattern(t))
    for i in result:
        print(i, end=" ")
        
if __name__ == "__main__":
    # text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    # k, d = 4, 1
    with open("rosalind_ba1j (2).txt", "r") as f:
        text = f.readline().strip()
        k, d = map(int, f.readline().strip().split())
    FindMostFrequentPattern(text, k, d)