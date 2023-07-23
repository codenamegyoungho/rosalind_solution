import numpy as np 
import pandas as pd 

with open('rosalind_cons (1).txt','r') as f:
    lines = f.read().strip().split('\n')
    info_list = []
    seq_list = []
    info = None 
    seq = ''
    for line in lines:
        if line.startswith('>'):
            if info and seq:
                info_list.append(info)
                seq_list.append(seq)
            info = line[1:]
            seq = ''
        else:
            seq += line
    if info and seq:
        info_list.append(info)
        seq_list.append(seq)



    seqs =  lines[1::2]
    arr = np.full((4,len(seq_list[0])),0)
    for s in seq_list:
        s = ''.join(s)
        for t in range(len(seq_list[0])): ##8개!
            if s[t] == 'A':
                arr[0,t] += 1
            elif s[t] == 'C':
                arr[1,t] += 1
            elif s[t] == 'G':
                arr[2,t] += 1 
            else:
                arr[3,t] += 1
    df = pd.DataFrame(arr,index=['A','C','G','T'])
    max_index = ''.join((df.idxmax()))
    print(max_index)
    
    a = df.loc['A']
    word = ''
    for i in range(len(a)):
        word += str(a[i])
    word1 = ' '.join(word)
    print('A:',word1)
    a = df.loc['C']
    word = ''
    for i in range(len(a)):
        word += str(a[i])
    word1 = ' '.join(word)
    print('C:',word1)
    a = df.loc['G']
    word = ''
    for i in range(len(a)):
        word += str(a[i])
    word1 = ' '.join(word)
    print('G:',word1)
    a = df.loc['T']
    word = ''
    for i in range(len(a)):
        word += str(a[i])
    word1 = ' '.join(word)
    print('T:',word1)
        
    