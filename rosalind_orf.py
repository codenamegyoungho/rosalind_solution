from Bio.Seq import Seq 


prob = ''
with open('rosalind_orf.txt','r') as f:
    info = f.readlines()
    for i in range(len(info)):
        info[i] = info[i][0:len(info[i])-1]

for i in info:
    if i.startswith('>'):
        pass
    else:
        prob += i
print(prob)




seq = Seq(prob)
answer = []
for i in range(len(seq)-2):
    # seq1_particle_list = []
    seq1 = seq[i:]
    seq1_particle_sum_translate = ''
    for j in range(0,len(seq1)-2,3):
        seq1_particle = seq1[j:j+3]
        # seq1_particle_list.append(seq1_particle)
        seq1_particle_sum_translate += seq1_particle.translate()
        start_indices = [i for i,char in enumerate(seq1_particle_sum_translate) if char =='M']
        stop_indices = [i for i,char in enumerate(seq1_particle_sum_translate) if char == '*']
        
        for mpoint in start_indices:
            end_idx = seq1_particle_sum_translate.find('*',mpoint)
            if end_idx != -1:
                answer.append(seq1_particle_sum_translate[mpoint:end_idx])

for i in range(0,len(seq)-2):
    seq2 = seq[0:len(seq)-i]
    seq2_particle_sum_translate = ''
    for j in range(0,len(seq2)-2,3):
        seq2_particle = seq2[j:j+3]
        seq2_particle_sum_translate += seq2_particle.translate()
        start_indices1 = [i for i,char in enumerate(seq2_particle_sum_translate) if char == 'M']
        
        for mpoint in start_indices1:
            end_idx1 = seq2_particle_sum_translate.find('*',mpoint)
            if end_idx1 != -1:
                answer.append(seq2_particle_sum_translate[mpoint:end_idx1])


from Bio.Seq import Seq 
seq = Seq(prob)
rev_seq = seq.reverse_complement()


for i in range(len(rev_seq)-2):

    # seq1_particle_list = []
    seq1 = rev_seq[i:]
    seq1_particle_sum_translate = ''
    for j in range(0,len(seq1)-2,3):
        seq1_particle = seq1[j:j+3]
        # seq1_particle_list.append(seq1_particle)
        seq1_particle_sum_translate += seq1_particle.translate()
        start_indices = [i for i,char in enumerate(seq1_particle_sum_translate) if char =='M']
        stop_indices = [i for i,char in enumerate(seq1_particle_sum_translate) if char == '*']
        
        for mpoint in start_indices:
            end_idx = seq1_particle_sum_translate.find('*',mpoint)
            if end_idx != -1:
                answer.append(seq1_particle_sum_translate[mpoint:end_idx])
for i in set(answer):
    print(i)