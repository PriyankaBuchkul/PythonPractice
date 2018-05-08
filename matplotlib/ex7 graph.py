import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

style.use('fivethirtyeight')
df = pd.read_csv('first_csv.csv')
st=sorted(df['Value'])

plt.plot(st)
plt.show()
