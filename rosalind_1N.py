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
a = find('CTAGAGCGA',3)
b = find('CTAGAGCGA',2)
c = find('CTAGAGCGA',1)
d = find('CTAGAGCGA',0)
answer = []
for i in a:
    answer.append(i)
for i in b:
    answer.append(i)
for i in c:
    answer.append(i)
for i in d:
    answer.append(i)

    with open('answer.txt','w') as f:
        for i in answer:
            f.write(i + '\n')