import pandas as pd

data = {'Duration': {'0': 60,
                     '1': 60,
                     '2': 23, },
        'Pulse': {'0': 110, '1': 103, '2': 117},
        'Calories': {'0': 38, '1': 479, '2': 300}}
df = pd.DataFrame(data)
#print(df)
# Info About the Data
print(df.info())