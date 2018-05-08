import numpy as np
Y=np.array([[3,4,5],[1,2,3],[6,7,8]])
for i in Y:
      print(i+3,id(i))

for y in np.nditer(Y,op_flags=['readwrite']):
      y+=3
      print(y,id(y))


