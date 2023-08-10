from Bio.Data import CodonTable 

codon_table = CodonTable.unambiguous_rna_by_name['Standard']
print(codon_table)

F,L,I,M,V,S,P,T,A,Y,H,Q,N,K,D,E,C,W,R,G = 2,6,3,1,4,6,4,4,4,2,2,2,2,2,2,2,2,1,6,4
with open('rosalind_mrna.txt','r') as f:
    entire_seq = f.read().strip()
    multi = 1
    for word in entire_seq:
        multi *= eval(word)
    multi *= 3
print(multi%1000000)