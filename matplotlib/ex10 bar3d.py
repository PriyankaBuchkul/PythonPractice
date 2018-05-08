from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

fig= plt.figure()
ax1=fig.add_subplot(111,projection='3d')

x3=[1,2,3,4,5,6,7,8,9,10]
y3=[5,6,7,8,2,5,6,3,7,2]
z3=np.zeros(10)

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3,y3,z3,dz,dy,dz)


ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')
ax1.set_zlabel('Z axis')
ax1.set_title('3d Bar Graph')
plt.show()
