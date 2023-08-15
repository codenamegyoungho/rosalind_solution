with open('rosalind_lgis.txt','r') as f:
    info = f.readline().strip()
    num = f.readline().strip().split()
    number = [int(i) for i in num]


# number = [5,1,4,2,3]
n = len(number)
li = [1]*n

#최장 증가 부분 수열
for i in range(1,n):
    for j in range(i):
        if number[i] > number[j]:
            li[i] = max(li[i],li[j] + 1) 


max_length = max(li)
increasing_subsequence = []

for i in range(len(number)-1,-1,-1):
    if li[i] == max_length:
        increasing_subsequence.append(str(number[i]))
        max_length -= 1 
#감소
li = [1]*n
for i in range(1,n):
    for j in range(i):
        if number[i] < number[j]:
            li[i] = max(li[i],li[j] + 1) 
max_length = max(li)
decreasing_subsequence = []

for i in range(len(number)-1,-1,-1):
    if li[i] == max_length:
        decreasing_subsequence.append(str(number[i]))
        max_length -= 1 

increasing_subsequence.reverse()
decreasing_subsequence.reverse()
print(" ".join(increasing_subsequence))
print(" ".join(decreasing_subsequence))

