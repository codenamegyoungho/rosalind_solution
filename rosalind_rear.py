with open('answer.txt','r') as f:
    #임시라인 생성 영어로 변수 만들어줘야함
    temp_line = []
    for line in f:
        temp_line.append(line.strip().split())
    lines = [item for item in temp_line if item != []]
    

def changing_index(line,change_length,index):
    cl = change_length
    new_line = line[:index] + line[index+cl-1:index-1:-1] + line[index+cl:]
    return new_line
print(changing_index([1,2,3,4,5,6,7,8,9],4,2))
def missmatching_index(line1,line2):
    diff = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            diff += 1
    return diff

for i in range(0,len(lines),2):
    line1 = lines[i]
    line2 = lines[i+1]
    change_length = 10
    min_diff = len(line1)
    while change_length > 1:
        for j in range(len(line2)-change_length+1):
            new_line2 = changing_index(line2,change_length,j)
            print(new_line2)
            # diff = missmatching_index(line1,new_line2)
            # if diff < min_diff:
            #     min_diff = diff
        change_length -= 1
 