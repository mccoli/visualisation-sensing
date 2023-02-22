import requests
import bs4
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/uk/'
# get string from specified web page
result = requests.get(url)

# create object that takes the long string from the web page and classifies different elements
soup = bs4.BeautifulSoup(result.text, 'lxml')

# get data out of the html class it is contained in
cases = soup.find_all('div', class_= 'maincounter-number')

# store the data
data = []

for i in cases:
    # getting the numbers only and storing them in the data array
    span = i.find('span')
    data.append(span.string)

print(data)

# create a dataframe (2d labelled structure with data mapped to it)
df = pd.DataFrame({'CoronaData' : data })
# column names
df.index = ({'TotalCases', 'Deaths', 'Recovered'})

# export data into excel
df.to_csv('Corona_Data.csv')