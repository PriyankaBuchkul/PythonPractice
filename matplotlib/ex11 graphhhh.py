from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

fig= plt.figure()
ax1=fig.add_subplot(111,projection='3d')

x,y,z=axes3d.get_test_data()

ax1.plot_wireframe(x,y,z,rstride=3,cstride=3)


ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')
ax1.set_zlabel('Z axis')
ax1.set_title('3d Bar Graph')
plt.show()



