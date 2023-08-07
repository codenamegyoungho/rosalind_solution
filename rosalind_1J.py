from Bio.Seq import Seq 


def find(target,hamming):
    result = []
    base = ['A','C','G','T']
    

    def ca(remain_distance,current_seq,index):
        remain = remain_distance
        if remain == 0:
            result.append(current_seq)
            return 

        for u in range(index,len(current_seq)):
            for char in base:
                if current_seq[u] != char:
                    new_seq = current_seq[:u] + char + current_seq[u+1:]
                    ca(remain_distance-1,new_seq,u+1)
    ca(hamming,target,0)
    return result




with open('rosalind_ba1j (1).txt','r') as f:
    seq = f.readline().strip()
    info = f.readline().strip().split()
    info = [int(i) for i in info]
fivethree = []

neighbors = []
rev_neighbors = []
neighbors_di = {}
rev_neighbors_di = {}
for i in range(len(seq)-info[0]+1):
    particle = Seq(seq[i:i+info[0]])
    fivethree.append(particle)
for part in fivethree:
    for number in range(info[1]+1):
        a = find(part,number)
        for s in a:
            neighbors.append(s)
for i in neighbors:
    # rev_neighbors.append(i[::-1])
    i = Seq(i)
    rev_neighbors.append(i.reverse_complement())


##fivethree neighbors is just easy way! 
for i in neighbors:
    gaesoo = 0
    for s in fivethree:
        count = 0
        for u in range(info[0]):
            if i[u] != s[u]:
                count += 1
        if count <= info[1]:
            gaesoo += 1               
    neighbors_di[i] = gaesoo


for i in rev_neighbors:
    gaesoo = 0
    for s in fivethree:
        count = 0
        for u in range(info[0]):
            if i[u] != s[u]:
                count += 1
        if count <= info[1]:
            gaesoo += 1               
    rev_neighbors_di[i] = gaesoo
sum_list = []
for kone,ktwo in zip(neighbors_di.keys(),rev_neighbors_di.keys()):
    sum = 0
    sum = neighbors_di[kone]+rev_neighbors_di[ktwo] 
    sum_list.append(sum)

for kone,ktwo in zip(neighbors_di.keys(),rev_neighbors_di.keys()):
    if neighbors_di[kone]+rev_neighbors_di[ktwo] == max(sum_list):
        print(kone,end= ' ') 








