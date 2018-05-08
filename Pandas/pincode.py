import pandas as pd
import sqlite3

conn=sqlite3.connect("pincode.db")
c=conn.cursor()
##
##def create_table():
##      c.execute("CREATE TABLE IF NOT EXISTS pincodedetails(id int,\
##                                                           officename vrchar,\
##                                                           pincode varchar,\
##                                                           officetype varchar,\
##                                                           Deliverystatus varchar,\
##                                                           divisionname varchar,\
##                                                           regionname varchar,\
##                                                           circlename,\
##                                                           taluk varchar,\
##                                                           districtname varchar,\
##                                                           statename varchar)")
##
##create_table()
df=pd.read_csv('pincode.csv',usecols=['statename','taluk','pincode'],skipinitialspace=True,encoding='ISO-8859-1')

for i in df.head():
                print(i)

#df.to_sql('pincodedetails',conn,if_exists='append',index=False)
                
