with open('rosalind_ba1i (5).txt','r') as f:
    seq = f.readline().strip()[:-1]
    info = f.readline().strip().split()
    for i in range(len(info)):
        info[i] = int(info[i])
    base = ['A','C','G','T']
    all = []
    from itertools import product
    result = list(product(base,repeat=info[0]))
    for i in result:
        i = ''.join(i)
        all.append(i)
    
    particle = []
    for i in range(len(seq)-info[0]+1):
        particle.append(seq[i:i+info[0]])
    answer = {}
    for i in all:
        for s in particle:
            count = 0
            for u in range(info[0]):
                if i[u] != s[u]:
                    count += 1
            if count <= info[1]:
                if i not in answer.keys():
                    answer[i] = 1
                else:
                    answer[i] += 1 
    for i in answer:
        if answer[i] == max(answer.values()):
            print(i,end = ' ')
    
