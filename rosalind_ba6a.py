import re
import pdb

with open('rosalind_ba6a.txt','r') as f:
    tuples = f.readline().strip()
    numbers = re.findall(r'[-+]\d+', tuples)
    # print(numbers)
def reversing_index(numbers,시작값,끝값):
    numbers = numbers[:시작값] + numbers[시작값:끝값+1][::-1] + numbers[끝값+1:]
    return numbers

def changing_부호(numbers,시작값,끝값):
    for i in range(시작값,끝값+1):
        if numbers[i][0] == '+':
            numbers[i] = '-' + numbers[i][1:]
        elif numbers[i][0] == '-':
            numbers[i] = '+' + numbers[i][1:]
    return numbers


시작값 = 0
with open('rosalind_ba6a_answer.txt','w') as f:
    for i in range(len(numbers)):
        
        원하는값 = i+1
        # pdb.set_trace()
        원하는값index = [i for i,value in enumerate(numbers) if 원하는값 == int(value[1:])]
        
        numbers = reversing_index(numbers,시작값,원하는값index[0])
        numbers = changing_부호(numbers,시작값,원하는값index[0])
        시작값 += 1
        f.write('('+' '.join(numbers)+')' + '\n') 
        if numbers[i][0] == '-':
            numbers[i] = '+' + numbers[i][1:]
            f.write('('+' '.join(numbers)+')' + '\n') 
