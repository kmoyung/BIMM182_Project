from Bio.SeqUtils.ProtParam import ProteinAnalysis
from pandas import DataFrame, read_csv
import pandas as pd

file = r'C:/Users/Kevin/Desktop/BIMM182_Project/Sequences.csv'
input = pd.read_csv(file)

instabilities = []

for i in range(len(input)):
    seq = input.iloc[i, 2]
    analysed_seq = ProteinAnalysis(seq)
    if analysed_seq.instability_index() >= 40:
        stable = "Unstable"
    else:
        stable = "Stable"
    entry = stable + ', ' + str(analysed_seq.instability_index())
    instabilities.append(entry)

results = {"Name":input.iloc[:, 0], "ProtParam":instabilities}
output = pd.DataFrame(data = results)

output.to_csv(r'C:/Users/Kevin/Desktop/BIMM182_Project/ProtParam.csv', header = ["ID", "ProtParam"], index = False, line_terminator = ',\n')


# test_seq = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEKNWFVGLKKNGSCKRGPRTHYGQKAILFLPLPV"
# analysed_seq = ProteinAnalysis(test_seq)
#
# # Calculate and output instability index. > 40 is unstable = short half life
# print(analysed_seq.instability_index())
