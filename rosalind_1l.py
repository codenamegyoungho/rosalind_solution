seq = 'CACGTTAAAAACCGTCTTCAAAGGT'
seq_length =  len(seq) - 1
A,C,G,T = 0,1,2,3
sum1 = 0
sum2 = 0

for i in range(len(seq)):
    sum1 += eval(seq[i])*4**(seq_length-i)
print(sum1)
