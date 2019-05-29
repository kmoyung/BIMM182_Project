# Kevin Moyung, Nha Do

"""
Fastaparse.py parses the entire Acinobacter baumanni organism and selects
100 proteins (from index 2000 - 2099)

Input: FASTA File of 3500 sequences (proteins)
Output: 100 IDs, their names, and the corresponding sequences
"""

from Bio import SeqIO
import pandas as pd

records = list(SeqIO.parse("C:/Users/Kevin/Desktop/BIMM182_Project/UP000006737.fasta", "fasta"))
subset = records[2000:2100]

ids = []
names = []
seqs = []

# Iterate through all 100 sequences
for i in range(len(subset)):
    # Store the IDs
    id = str.split(subset[i].id, ':')
    id = id[1]
    ids.append(id)

    # Store the names
    name = str.split(subset[i].description, 'OS')
    name = name[0]
    names.append(name[18:])

    # Store the sequences
    seqs.append(subset[i].seq)

d = {'ID':ids, 'Name':names, 'Sequence':seqs}
output = pd.DataFrame(data = d)

output.to_csv(r'C:/Users/Kevin/Desktop/BIMM182_Project/Sequences.csv', header = ["ID", "Name", "Sequence"], index = None)
