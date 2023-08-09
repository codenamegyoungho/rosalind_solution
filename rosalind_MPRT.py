import requests 
import re
from Bio import SeqIO 
from io import StringIO
shortname = []
fullname = []
with open('rosalind_mprt (1).txt','r') as f:
    for line in f:
        shortname.append(line[0:6])
        fullname.append(line[0:len(line)-1])
print(shortname,fullname)


for i in range(len(shortname)):

    uniprot_id = shortname[i]
    
    url = f'https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta'
    response = requests.get(url)
    data = response.text
    data_stream = StringIO(data)

    sequence_record = SeqIO.read(data_stream,'fasta')
    sequence = str(sequence_record.seq)
    motif = re.compile('(?=N[^P][ST][^P])')
    matches = motif.finditer(sequence)
    if shortname[i] == fullname[i]:
        print(shortname[i])
    else:
        print(fullname[i])
    for match in matches:
            start = match.start()
            print(start+1,end = ' ')
    print('')
            