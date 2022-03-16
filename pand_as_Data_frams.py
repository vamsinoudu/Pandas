import pandas as pd

lst = ['pandas ', 'in python ', 'not that difficult']
df = pd.DataFrame(lst)
print(df)

data = pd.read_csv("C:\\Users\\vamsi\\Downloads\\myexcel.csv", index_col='Name')
data.drop(["Avery Bradley"], inplace=False)
print(data)

