import math
def base_count(seq,):
    """Return the number of each base in a sequence."""
    seq.count('A') + seq.count('T')
    seq.count('G') + seq.count('C')
    return seq.count('A')+seq.count('T'), seq.count('G')+ seq.count('C')

def prob_finding(gc_content):
    """Return the probability of finding a random string in a sequence."""
    gc = gc_content/2 
    at = (1 - gc_content)/2
    return at,gc
def main(seq,gc_contents):
    answer = []
    """Return the log of the probability of finding a random string in a sequence."""
    for gc_content in gc_contents:
        at,gc = prob_finding(gc_content)
        prob = (at**seq.count('A'))*(at**seq.count('T'))*(gc**seq.count('G'))*(gc**seq.count('C'))
        common_logarithm = float(round(math.log10(prob),3))
        answer.append(common_logarithm) 
    return print(*answer, sep=' ')

if __name__ == '__main__':
    with open('rosalind_prob.txt','r') as f:
        seq = f.readline().strip()
        gc_contents = f.readline().strip().split()
        gc_contents = [float(i) for i in gc_contents]
        main(seq,gc_contents)
        