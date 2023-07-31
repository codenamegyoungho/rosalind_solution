with open('rosalind_iev (1).txt','r') as f:
    info = f.readline().strip().split()
    for i in range(len(info)):
        info[i] = float(info[i])
    a = info[0]*2
    b = info[1]*2
    c = info[2]*2
    d = info[3]*0.75*2
    e = info[4]*0.5*2
    f = info[5]*0*2
    print(a+b+c+d+e+f)