import pandas as pd

web_stats={'Day':[1,2,3,4,5],
           'visitors':[21,34,56,78,12],
           'Bounce Rate':[65,77,89,23,12]}


df=pd.DataFrame(web_stats)
print(df.head(2))



l=[[2131,3,34],[4,5,67,89],[5,34,2,22,1]]
df1=pd.DataFrame(l)
print(df1)
