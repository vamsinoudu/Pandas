import pandas as pd

df = pd.read_csv("C:\\Users\\vamsi\\Downloads\\myexcel.csv")
df_stacked = df.stack()
print(df_stacked.tail(26))     # Head OR Tail
