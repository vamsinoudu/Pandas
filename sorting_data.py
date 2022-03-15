import pandas as pd

data = {'Brand': ['HH', 'TT', 'FF', 'AA'],
        'Price': [22000, 25000, 27000, 35000],
        'Year': [2015, 2013, 2018, 2018]
        }

df = pd.DataFrame(data, columns=['Brand', 'Price', 'Year'])

# sort Brand in an ascending order
df.sort_values(by=['Year'], inplace=True)

print(df)
