# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("C:\\Users\\vamsi\\Downloads\\myexcel.csv")

# First grouping based on "Team"
# Within each team we are grouping based on "Position"
gkk = df.groupby(['Team', 'Position'])

# Print the first value in each group
print(gkk.first())
