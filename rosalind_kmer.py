from Bio import SeqIO 
from itertools import product
with open('rosalind_kmer.txt','r') as f:
    raw = SeqIO.read(f,'fasta')
    seq =raw.seq
base_lex = ['A','C','G','T']

def making_kmer(seq):
    kmer = []
    for i in range(len(seq)-3):
        kmer.append(seq[i:i+4])
    return kmer
kmer = making_kmer(seq)
kmer_lex = [''.join(i) for i in product(base_lex,repeat=4)]
kmer_count = [kmer.count(i) for i in kmer_lex]
print(' '.join([str(i) for i in kmer_count]))
