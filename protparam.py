from Bio.SeqUtils.ProtParam import ProteinAnalysis
from pandas import DataFrame, read_csv
import pandas as pd

file = r'C:/Users/Kevin/Desktop/BIMM182_Project/Sequences.csv'
input = pd.read_csv(file)

# print(input[2][2])
# 
# test_seq = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEKNWFVGLKKNGSCKRGPRTHYGQKAILFLPLPV"
# analysed_seq = ProteinAnalysis(test_seq)
#
# # Calculate and output instability index. > 40 is unstable = short half life
# print(analysed_seq.instability_index())
