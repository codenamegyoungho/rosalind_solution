from Bio.Seq import Seq 
word = ''
with open('rosalind_revp.txt','r') as f:
    for line in f:
        if line.startswith('>'):
            pass 
        else:
            word += line[:len(line)-1]
print(word)
seq = Seq(word)
print(len(seq))
print(seq)
print(seq.complement())

def finding_palindrome(number):
    for i in range(len(seq)-number+1):
        particle = seq[i:i+number]
        rev_particle = particle.reverse_complement()
        if particle == rev_particle:
            print(i+1,number)

for i in range(4,13):
    finding_palindrome(i)

