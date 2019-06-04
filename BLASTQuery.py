# Kevin Moyung, Nha Do

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from pandas import DataFrame, read_csv
import pandas as pd

file = r'C:/Users/Kevin/Desktop/BIMM182_Project/Sequences.csv'
input = pd.read_csv(file)

results = []

for i in range(45,56):
    sequence = input.iloc[i, 2]

    # Run BLAST against UniProt/Swiss-Prot Database
    result_handle = NCBIWWW.qblast("blastp", "swissprot", sequence, alignments = 1, descriptions = 1, hitlist_size = 1)
    blast_result = NCBIXML.read(result_handle)

    alignment = blast_result.alignments[0]
    name = alignment.title
    name = str.split(name, '=')
    name = name[1]
    name = str.split(name, ';')
    name = name[0]

    results.append(name)


res = {"Name":input.iloc[45:56, 0], "BLAST":results}
output = pd.DataFrame(data = res)

output.to_csv(r'C:/Users/Kevin/Desktop/BIMM182_Project/BLAST.csv', header = ["ID", "BLAST"], index = False, line_terminator = ',\n')
