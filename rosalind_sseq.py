with open('rosalind_sseq.txt','r') as f:
    seqs = []
    seq = ''
    for line in f:
        if line.startswith('>'):
            if seq:
                seqs.append(seq)
                seq = ''
        else:
            seq += line.strip()
    if seq:
        seqs.append(seq)
def finding_spliced_motif(seqs):
    s = seqs[0]
    t = seqs[1]
    first_index = -1
    index_list = []
    for i in range(len(t)):
        first_index = s.find(t[i],first_index+1)
        index_list.append(first_index+1)
    return index_list
print(*finding_spliced_motif(seqs))