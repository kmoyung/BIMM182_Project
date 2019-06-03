# Kevin Moyung, Nha Do

from Bio import ExPASy
from Bio.ExPASy import ScanProsite
from pandas import DataFrame, read_csv
import pandas as pd

file = r'C:/Users/Kevin/Desktop/BIMM182_Project/Sequences.csv'
input = pd.read_csv(file)

motifset = []

for i in range(len(input)):
    sequence = input.iloc[i, 2]

    accessions = set()
    motifs = ""

    # Scan Prosite for matching motifs
    handle = ScanProsite.scan(seq = sequence, skip = "off")
    result = ScanProsite.read(handle)

    # Obtain all accession motifs
    for hit in result:
        acc = hit.get('signature_ac')
        accessions.add(acc)

        # Get descriptions from accession numbers
    for accession in accessions:
        prof = ExPASy.get_prosite_raw(accession)
        text = prof.read()
        text = text.splitlines()
        desc = text[3]
        desc = str.split(desc, 'DE   ')
        desc = desc[1]
        desc = desc[0:(len(desc) - 1)]

        motifs += desc + ";"

    motifs = motifs[0:(len(motifs) - 1)]
    motifset.append(motifs)

results = {"Name":input.iloc[:, 0], "Prosite":motifset}
output = pd.DataFrame(data = results)

output.to_csv(r'C:/Users/Kevin/Desktop/BIMM182_Project/Prosite.csv', header = ["ID", "Prosite"], index = False, line_terminator = ',\n')
