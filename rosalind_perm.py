from itertools import permutations 
number = 7
number_list = [] 
number_list2 = []
for i in range(1,number+1):
    number_list.append(str(i))

a = list(permutations(number_list,r=number))

print(len(a))
for i in a:
    number_list2.append(' '.join(i))
# for i in number_list2:
#     print(i)
with open('answer.txt','w') as f:
    for i in number_list2:
        f.write(i+'\n')
