with open('rosalind_ba1h (9).txt','r') as f:
    lines = f.read().strip().split('\n')
    info = []
    seqs = []
    seq = ''
    num = []
    sp = []
    cd = {}
    for line in lines:
        if line.startswith('>'):
            info.append(line[1:])
        elif line.startswith('#'):
            num.append(int(line[1:]))
        else:
            seq += line
            seqs.append(seq)

    
    
    for i in range(len(seqs[0])-len(info[0])+1):
        sp.append(seqs[0][i:i+len(info[0])])
    
    # for k in range(len(sp)):
    #     for s in range(len(sp[0])):    
    #         if sp[k][s] != info[0][s]:
    #             if sp[k] not in cd.keys():
    #                 cd[sp[k]] = 1
    #             else:
    #                 cd[sp[k]] += 1
    #         elif sp[k][s] == info[0][s]:
    #             if sp[k] not in cd.keys():
    #                 cd[sp[k]] = 0


        # if cd[sp[k]] <= num[0]:
        #      print(k,end = ' ')

    
    


    list2 = []
    ####중복제거 ㄱㄱ
    for k in range(len(sp)):
            count = 0
            for s in range(len(sp[0])):    
                if sp[k][s] != info[0][s]:
                    count += 1 
                elif sp[k][s] == info[0][s]:
                    count += 0
            list2.append(count)
    answer_final = dict(zip(sp,list2))
    
    for k in range(len(sp)):
        if answer_final[sp[k]] <= num[0]:
            print(k,end =' ')