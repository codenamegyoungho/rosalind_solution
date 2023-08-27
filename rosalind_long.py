def get_overlap_strings(s1,s2):
    combine_strings = []
    overlap_strings = []
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1)-i]:
            overlap_strings.append(s1[i:])
            combine_strings.append(s1+s2[len(s1)-i:])
            break
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2)-i]:
            overlap_strings.append(s2[i:])
            combine_strings.append(s2+s1[len(s2)-i:])
            break
    if not overlap_strings:
        return "", ""
    combine_string = min(combine_strings,key=len)
    overlap_string = max(overlap_strings,key=len)
    return combine_string,overlap_string





def finding_shortest_superstring(dnas):
    temp = dnas 
    while len(dnas) > 1:
        max_overlapping = ''
        max_combining = ''
        max_overlapping_length = 0
        for i in range(len(temp)-1):
            for j in range(i+1,len(temp)):
                combine_string,overlap_string = get_overlap_strings(temp[i],temp[j])
                if len(overlap_string) > max_overlapping_length:
                    max_overlapping = combine_string
                    max_overlapping_pair = [temp[i],temp[j]]
                    max_overlapping_length = len(overlap_string)
        temp.remove(max_overlapping_pair[0])
        temp.remove(max_overlapping_pair[1])
        temp.append(max_overlapping)
    return temp 

with open('rosalind_long.txt','r') as f:
    dnas = []
    word = ''
    for line in f:
        if line.startswith('>'):
            if word:
                dnas.append(word)
                word = ''
        else:
            word += line.strip()
    dnas.append(word)
print(finding_shortest_superstring(dnas)[0])