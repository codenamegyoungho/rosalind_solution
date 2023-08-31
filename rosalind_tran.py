def finding_tran(seqs):
    transition_count = 0
    transversion_count = 0
    transitions = ['AG','GA','CT','TC']
    transversions = ['AC','CA','AT','TA','GC','CG','GT','TG']
    for i in range(len(seqs[0])):
        if seqs[0][i]  == seqs[1][i]:
            continue
        else:
            if seqs[0][i] + seqs[1][i] in transitions:
                transition_count += 1
            elif seqs[0][i] + seqs[1][i] in transversions:
                transversion_count += 1
    return transition_count/transversion_count

with open('rosalind_tran.txt','r') as f:
    seqs = []
    seq = ''
    for line in f:
        if line.startswith('>'):
            if seq:
                seqs.append(seq)
                seq = ''
        else:
            seq += line.strip()
    seqs.append(seq)
answer = finding_tran(seqs)
print(answer)