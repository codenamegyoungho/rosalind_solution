##Finding a shared Motif
with open('rosalind_lcsm (3).txt','r') as f:
    info = []
    seqs = []
    seq = ''
    for line in f:
        if line.startswith('>'):
            info.append(line[1:len(line)-1])
            if seq:

                seqs.append(seq)
                seq = ''
        else:
            seq += line[:len(line)-1] 
    seqs.append(seq)
a = 0
for k in range(1,len(seqs[0])):
    first = []
    n = k
    for j in range(len(seqs[0])-n+1):
        particle = seqs[0][j:j+n]
        first.append(particle)
    second = []
    for i in first:
        count = 0
        for j in seqs:
            if i in j:
                count += 1 
        if count == len(seqs):
            second.append(i)
    if second:
        print(second)       

    else:
        a += k-1
        break



