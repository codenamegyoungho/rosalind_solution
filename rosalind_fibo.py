rist = [0,1,1]
n = 90
m =18
for i in range(1,n+1):
    if 3 <= i <= m:
        rist.append(sum(rist[i-2:i-1+1]))
    elif i > m:
        rist.append(sum(rist[i-m:i-1]))
print(rist)

