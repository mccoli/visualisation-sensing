import pandas as pd

df = pd.read_csv('imdbTop250.csv')
# creates new df without rows that contain empty cells
new_df = df.dropna()
# with inplace argument, it changes original dataframe
# new_df = df.dropna(inplace = True)
print(new_df.info())

# replaces all null values with the number 130
new_df = df.fillna(130)
# replaces empty values in specified column
new_df = df["Ranking"].fillna(5)
print(new_df.info())

# u can also replace empty cells with the mean, median or mode of the column
x = df["Ranking"].mean()
df["Ranking"].fillna(x, inplace = True)
# print(df.info())

# you may need to correct formats or change data that was a typo or other error
# if the dataset is small enough you can change individual values
# or you can create some rules based on how you expect the data to appear and replace any values that don't follow the rules
# or you can remove rows that do not fit the rules

# returns True for every row that is a duplicate
# print(df.duplicated())
df.drop_duplicates(inplace = True)

# shows the relationships between columns (ignores non numeric)
# varies from -1 to 1. 0.9 is a good relationship, if you increase x, y will also increase. -0.9: if you decrease x, y will also decrease. 0.2 is a bad relationship: if x goes up, y probably will not.
print(df.corr())