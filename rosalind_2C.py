with open('rosalind_ba2c.txt','r') as f:
    data = f.read()
lines = data.split('\n')
seqs = lines[0]
num = int(lines[1]) 
matrix_lines = lines[2:]
matrix = [list(map(float,line.split())) for line in matrix_lines]
transposed_matrix = list(map(list,zip(*matrix)))
seq_multiple = []
print('matrix',matrix)
print('transposed',transposed_matrix)
for i in range(len(seqs)-num+1):
    seq_particle = seqs[i:i+num]
    multiple = 1
    for seq_num in range(num):
        if seq_particle[seq_num] == 'A':
            multiple *= transposed_matrix[seq_num][0]
        elif seq_particle[seq_num] == 'C':
            multiple *= transposed_matrix[seq_num][1]
        elif seq_particle[seq_num] == 'G':
            multiple *= transposed_matrix[seq_num][2]
        elif seq_particle[seq_num] == 'T':
            multiple *= transposed_matrix[seq_num][3]
    seq_multiple.append((seq_particle,multiple))
max_value = max(seq_multiple,key=lambda x: x[1])
print(max_value[0])
