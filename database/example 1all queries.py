import sqlite3
import random
import time
import datetime

conn=sqlite3.connect('D-mart1.db')#connection to database
c=conn.cursor()#cursor =points and performs action
def create_table():
      c.execute("create table toothpaste(id int,date date,brand text,prize int ,discount float)")

#create_table()

def create_new_table():
      c.execute("create table toothpasteind(brand text,location text)")
#create_new_table()
def insert_entry_new():
      l1=['Patanjali','babul','closeUp','Himalaya','Dabarred','Ultra Brite','Aquafresh','Miswak']
      loc=['pune','Mumbai','Banglore','Hydrabad']
      brand1=random.choice(l1)
      location1=random.choice(loc)
      c.execute("insert into toothpasteind(brand,location)values(?,?)",(brand1,location1))
      conn.commit()
      #c.close()
      #conn.close()
for i in range(10):
      #insert_entry_new()
      time.sleep(1)


def dynamic_entry():
      l1=['Patanjali','babul','closeUp','Himalaya','Dabarred','Ultra Brite','Aquafresh','Miswak']
      l2=[4,5,6,7,8,9,10,11,12,13,14]
      id1=random.choice(l2)
      date=datetime.date(random.randint(2017,2017),random.randint(1,12),random.randint(1,31))#single element RANDINT
      prize=random.randrange(40,160)#rang RANDRANGE
      discount=random.randrange(10,55)
      brand=random.choice(l1)
      c.execute("insert into toothpaste(id,date,brand,prize,discount)values(?,?,?,?,?)",(id1,date,brand,prize,discount))
      conn.commit()
for i in range(11):
     # dynamic_entry()
      time.sleep(1)

def natural_join():
      for i in list(c.execute("select * from toothpaste natural join toothpasteind")):
            print(i)
      conn.commit()
      c.close()
#natural_join()


def inner_join():
      for i in list(c.execute("select * from toothpaste left join toothpasteind on toothpaste.brand=toothpasteind.brand")):
            print(i)
   #   conn.commit()
      c.close()
inner_join()






















