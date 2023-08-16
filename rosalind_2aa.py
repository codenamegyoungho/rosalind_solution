import re
검사기 = re.compile('[a-zA-Z]')
seqs모음집 = []
info = []
with open('rosalind_ba2a.txt','r') as f:
    for line in f:
        if 검사기.match(line):
            seqs모음집.append(line.strip())
        else:
            info = [int(i) for i in line.strip().split()]
base = 'ACGT'
def finding(target,remaining_dist):
    remain = remaining_dist
    result = []
    
    def finding_neighbors(target,remaining_dist,index):
        remain = remaining_dist
        if remain == 0:
            result.append(target)
            return
        for i in range(index,len(target)):
            for char in base:
                if target[i] != char:
                    # remaining_dist -= 1 
                    new_seq = target[:i] + char + target[i+1:]
                    # index = i+1
                    finding_neighbors(new_seq,remaining_dist-1,i+1)
    finding_neighbors(target,remaining_dist,0)
    return result
target_모음집 = [seqs모음집[0][i:i+info[0]] for i in range(len(seqs모음집[0])-info[0]+1)]
neighbors= []


for i in target_모음집:
    for j in range(info[1]+1):
        a = finding(i,j)
        neighbors.extend(a)




# 검사
check여부 = {}

for neighbor in neighbors:
    neighbor_found = False  # 현재 neighbor에 대한 검사 결과
    for seqs in seqs모음집:
        seq_found = False  # 현재 시퀀스에 대한 검사 결과
        for k in range(len(seqs) - info[0] + 1):
            seq_particle = seqs[k:k + info[0]]
            count = 0
            for u in range(info[0]):
                if seq_particle[u] != neighbor[u]:
                    count += 1
            if count <= info[1]:
                seq_found = True  # 시퀀스에 대해 조건을 만족하는 경우
                break  # 해당 시퀀스에서 조건을 만족하는 부분이 발견되면 중단
        if not seq_found:
            break  # 시퀀스에 대해 조건을 만족하는 부분이 발견되지 않으면 중단
    if seq_found:
        check여부[neighbor] = True
    else:
        check여부[neighbor] = False
print(check여부)
# 검사 결과 출력
for neighbor, found in check여부.items():
    if found:
        print(neighbor)