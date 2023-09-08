from Bio import SeqIO
with open('rosalind_lgis.txt','r') as f:
    raw = SeqIO.parse(f,'fasta')
    seq = next(raw).seq
kmp = [0]*len(seq)
for i in range(1,len(seq)):
    k = kmp[i-1]
    while k > 0 and seq[k] != seq[i]:
        k = kmp[k-1]
    if seq[k] == seq[i]:
        k += 1
    kmp[i] = k
    
with open('rosalind_kmp_ans.txt','w') as f:
    f.write(' '.join(map(str,kmp)))