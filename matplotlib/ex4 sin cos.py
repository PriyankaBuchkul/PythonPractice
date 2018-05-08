import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,5,0.1);
y=np.sin(x)
z=np.cos(x)



plt.plot(y)
plt.plot(z)

plt.show()
