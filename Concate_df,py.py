import pandas as pd
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

# Define a dictionary containing employee data
data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

print(df, "\n\n", df1)
# using a .concat() method
frames = [df, df1]

res1 = pd.concat(frames)
print(res1)
