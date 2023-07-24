with open('rosalind_grph (1).txt','r') as f:
    lines = f.read().strip().split('\n')
    info = []
    seqs = []
    seq = ''
    for line in lines:
        if line.startswith('>'):
            info.append(line)
            
            if seq:
                seqs.append(seq)
                seq = ''
        else:
            seq += line

    seqs.append(seq)

tu = list(zip(info,seqs))
front_info = []
front_seq = []
back_앞 = []
back_뒤 = []
#####뒤를 기준으로 앞을 분석
for i in range(len(tu)):##5개!
    for s in range(1,len(tu)):
        if tu[i][1][len(tu[i][1])-3:] == tu[s][1][0:3]:
            front_info.append(tu[i][0])
            front_seq.append(tu[s][0])
            # front.append(f'{tu[i]}:{tu[s]}')
        else:
            continue
front = list(zip(front_info,front_seq))
지울거1 = []   ##################################
print('front:',front)
for i in range(len(front)):     ###여기수정
    if front[i][0] == front[i][1]:
        # front.remove(front[i])
        지울거1.append(front[i])
print('지울거1:',지울거1)   #############################
for i in 지울거1:
    front.remove(i)


####앞을 기준으로 뒤를 분석
for i in range(len(tu)):##5개!
    for s in range(1,len(tu)):     
        if tu[i][1][0:3] == tu[s][1][len(tu[s][1])-3:]:
            back_뒤.append(tu[s][0])
            back_앞.append(tu[i][0])
            
            # front.append(f'{tu[i]}:{tu[s]}')
        else:
            continue
지울거2 = []    #############################3
back = list(zip(back_뒤,back_앞))
for i in range(len(back)):  ###여기수정
    if back[i][0] == back[i][1]:
        # back.remove(back[i])
        지울거2.append(back[i]) ###################
print('지울거2:',지울거2)

for i in 지울거2:
    back.remove(i)

front += back 
front = list(set(front))
print(front)
for i in range(len(front)):
    for s in range(len(front[i])-1):
        print(front[i][s][1:],front[i][s+1][1:])


        