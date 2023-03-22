import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdbTop250.csv')
df.plot()
plt.show()