def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    most_probable_kmer = ""
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[kmer[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
            
    return most_probable_kmer

def form_profile(motifs):
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    motif_count = len(motifs)
    motif_length = len(motifs[0])
    
    for base in profile:
        profile[base] = [0] * motif_length
    
    for i in range(motif_length):
        for motif in motifs:
            profile[motif[i]][i] += 1 / motif_count
            
    return profile

def score(motifs):
    consensus = ""
    motif_length = len(motifs[0])
    total_score = 0
    
    for i in range(motif_length):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            counts[motif[i]] += 1
        max_count = max(counts.values())
        total_score += len(motifs) - max_count
    
        consensus += max(counts, key=counts.get)
    
    return total_score

def greedy_motif_search(dna, k, t):
    best_motifs = [string[:k] for string in dna]
    
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]
        
        for j in range(1, t):
            profile = form_profile(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs

# Read input
with open("input.txt", "r") as file:
    k, t = map(int, file.readline().split())
    dna = [line.strip() for line in file]

# Run the algorithm
best_motifs = greedy_motif_search(dna, k, t)

# Print the result
for motif in best_motifs:
    print(motif)
