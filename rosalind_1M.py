number = 7
seq_length =  number - 1
A,C,G,T = 0,1,2,3
sum2 = 5335
word = ''

for i in range(number):
    몫 = sum2//4**(seq_length-i)
    sum2 -= 몫*4**(seq_length-i)
    if 몫 == 0:
        word += 'A'
    elif 몫 ==1:
        word += 'C'
    elif 몫 ==2:
        word += 'G'
    elif 몫 ==3:
        word += 'T'
print(word)

