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

with open('rosalind_ba1i (6).txt','r') as f:
    a = []
    seq = f.readline().strip()
    info = f.readline().strip().split()
    for i in range(len(info)):
        info[i] = int(info[i])
    for i in range(len(seq)-info[0]+1):
        particle = seq[i:i+info[0]]
        for s in range(info[1]+1):
            for u in find(particle,s):
                a.append(u)
    a = set(a)
    answer = {}
    for i in range(len(seq)-info[0]+1):
        particle = seq[i:i+info[0]]
        for s in a:
            count = 0
            for u in range(info[0]):
                if particle[u] != s[u]:
                    count += 1
            if count <= info[1]:
                if s not in answer:
                    answer[s] = 1
                else:
                    answer[s] += 1
    for i in answer:
        if answer[i] == max(answer.values()):
            print(i,end = ' ')
