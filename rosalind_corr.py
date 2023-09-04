from Bio import SeqIO 
seqs = []
with open('rosalind_corr.txt','r') as f:
    raw = SeqIO.parse(f,'fasta')
    for i in raw:
        seqs.append(i.seq)
def correct_incorrect(seqs):
    correct = []
    incorrect = []
    for i in seqs:
        if seqs.count(i) + seqs.count(i.reverse_complement()) > 1:
            correct.append(i)
        else:
            incorrect.append(i)
    return correct, incorrect
correct, incorrect = correct_incorrect(seqs)

def reverse_complement_list(correct):
    correct_rc = []
    for i in correct:
        correct_rc.append(i.reverse_complement())
    return correct_rc
correct_rc = reverse_complement_list(correct)
correct = correct + correct_rc

def hamming_dist(seq1,seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

def corr_error(incorrect, correct):
    corr = []
    for i in incorrect:
        for j in set(correct):
            if hamming_dist(i,j) == 1:
                corr.append((i,j))
    return set(corr)

corr = corr_error(incorrect, correct)
for i in corr:
    print(i[0],'->',i[1],sep='')