from Bio import SeqIO
with open('rosalind_pdst.txt','r') as f:
    raw = SeqIO.parse(f,'fasta')
    seqs = [str(i.seq) for i in raw]
    seqs_count = len(seqs)
matrix_seq = [[0 for i in range(seqs_count)] for j in range(len(seqs))]

def compare_distance_seq(seq1,seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance/len(seq1)
print(matrix_seq)
for i in range(len(seqs)):
    for j in range(len(seqs)):
        matrix_seq[i][j] = compare_distance_seq(seqs[i],seqs[j])
formatted_data = []
for row in matrix_seq:
    formatted_row = ['{:.5f}'.format(i) for i in row]
    formatted_data.append(formatted_row)
print('\n'.join([' '.join(i) for i in formatted_data]))