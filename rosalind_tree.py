with open('rosalind_tree.txt','r') as f:
    nodes = int(f.readline().strip())
    edges = [line.strip().split() for line in f.readlines()]
def calculate_need_edges(nodes, edges):
    return nodes - len(edges) - 1
print(calculate_need_edges(nodes, edges))