#hospital data Output data
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt


conn=sqlite3.connect("EOD.db")
c=conn.cursor()
def create_table():
      c.execute("CREATE TABLE IF NOT EXISTS EODdetails(id int,\
                                                           Date Date,\
                                                           Open varchar,\
                                                           High varchar,\
                                                           Low varchar,\
                                                           Close varchar,\
                                                           Adj_Volume varchar,\
                                                           Adj_Open varchar,\
                                                           Adj_High varchar)")

#create_table()

df=pd.read_csv('EOD-V.csv',usecols=['Date','Open','High','Low','Close','Adj_Volume','Adj_Open','Adj_High'])
print(df.head())

##
##s=df['Adj_High']
##df['Adj_High'.plot()]
##plt.legend()
##plt.show()

# append data to sqlite database
#df.to_sql('EOD',conn,if_exists='append',index=False)
                
'''
df12=np.reshape(np.array(df['open']),(len(df['open']),1))
print(df12)

df1=df['Adj_Open']
df2=df['Adj_High']
df3=df['Adj_Volume']
print(df1,df2,df3)
'''

