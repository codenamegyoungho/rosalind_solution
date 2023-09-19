import time 
def abs(num):
    return num if num > 0 else -num

def greedy_sorting(perm):
    result = []
    length = len(perm)
    i = 0
    comp = sorted(list(map(lambda x: x if x >= 0 else -x, perm)))
    while i < length:
        if abs(comp[i]) != perm[i]:
            idx = perm.index(comp[i]) if perm.count(comp[i]) else perm.index(-comp[i])
            perm = perm[:i] + [-x for x in perm[i:idx+1][::-1]] + perm[idx+1:]
            result.append(perm)
            if perm[i] < 0:
                perm = perm[:i] + [-perm[i]] + perm[i+1:]
                result.append(perm)
        i += 1
    return result

def ugly_print(lls):
    for ls in lls:
        line = []
        for num in ls:
            if num > 0:
                line.append('+' + str(num))
            else:
                line.append(str(num))
        print('(' + ' '.join(line) + ')')



def main():
    with open('rosalind_ba6a.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]
        perm_str = lines[0].strip('(').strip(')').split()
        perm_int = list(map(int, perm_str))
        

    lls = greedy_sorting(perm_int)
    ugly_print(lls)
# print(main())


if __name__ == '__main__':
    main()