import pandas as pd

# a series is like a column in a table
a = [1, 4, 7]
# add index argument to name your labels
myvar = pd.Series(a, index = ["first", "second", "third"])
# print(series)
# print(series["second"])
# print(series[0])

# create a series from a dictionary
# keys of the dictionaries become labels
calories = {"day1": 400, "day2": 600, "day3": 300}
myvar = pd.Series(calories)
# print(myvar)

# dataframes are multi-dimensional tables
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
# print(myvar)
# # returns one or more specified rows, can also find named index
# print(myvar.loc[0])
# print(myvar.loc[[0, 1]])

# change the num of rows displayed instead of the default first 5 and last 5 
# pd.options.display.max_rows = 5
df = pd.read_csv('imdbTop250.csv')
# returns headers w specified num of rows
print(df.head(10))
print(df.tail())
print(df.info())