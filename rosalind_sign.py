from itertools import permutations 
from itertools import product
import math
def absolute_formating(number):
    absolute_number_list = []
    for i in range(1,number+1):
        c,d = i,-i 
        absolute_number_list.append([c,d])
    return absolute_number_list 
answer = []
# print(absolute_formating(3))
combination_list = list(product(*absolute_formating(6)))
for i in combination_list:
    a = permutations(i,6)
    answer.append(list(a))
print(math.factorial(6)*len(answer))

with open('answer.txt','w') as f:
    f.write(str(math.factorial(6)*len(answer))+'\n')
    for i in answer:
        for j in i:
            f.write(' '.join(map(str,j))+'\n')

