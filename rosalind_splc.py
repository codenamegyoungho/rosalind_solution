import re 
from Bio.Seq import Seq 
seq = ''
seeq = ''
introns = []
with open('rosalind_splc (1).txt','r') as f:
    for line in f:
        if line.startswith('>Rosalind_6041'):
            is_first_seq = True
        elif line.startswith('>'):
            is_first_seq = False 
        elif is_first_seq:
            seq += line.strip()
        else:
            introns.append(line.strip())
print(seq)
print(introns)


pattern = '|'.join(re.escape(i) for i in introns)
result = re.split(pattern,seq)
answer = ''
for i in result:
    answer += i
answer = Seq(answer)
print(answer.translate(to_stop=True))
