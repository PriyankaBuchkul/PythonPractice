import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rand_horse = np.random.random_integers(1,101,size=(5,5))
faster_horse=np.amax(rand_horse)

iterations=0
df=pd.DataFrame(rand_horse)
print("Using Dataframses : \n",df)

count,bins,ignored =plt.hist(df,11,nprmed=True)

rows,sols=rand_horse.shape
for i in range(rows):
      rand_horse[i][::-1].sort()
      iterations+=1
df=pd.DataFrame(rand_horse)
print("Sorted by Rows :\n",df)
print("No of Races :\n",iterations)
i=np.lexsort((rand_horse[:,-1],rand_horse[:,0]))
b=rand_horse[i]
a=b[::-1]
iterations+=1
df=pd.DataFrame(a)
print("Sorted By Columns :\n",df)
print("Sorted By Races :\n",iterations)

rows,cols=a.shape
second=[]
for i in range(rows):
      second.append(np.max(np.partition(a,i)[i]))


print("Fastest Faster ",max(second))

print("second  ",second[1])
iterations+=1
print("Third Faster ",second[2])
print("Fourth Faster ",second[3])
print("Fifth Faster ",second[4])

print("No Of races:\n ",iterations)

plt.show()















      
