import pandas as pd

df = pd.read_csv("Ancestry_hg38.tsv",sep="\t")
df.to_excel("Ancestry_hg38_unsup",index=True)
