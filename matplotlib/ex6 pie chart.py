import matplotlib.pyplot as plt

slices =[7,2,2,13]
activities= ['sleeping','eating','working','playing']
cols=['c','m','r','g']

plt.pie(slices, labels=activities,
        colors=cols ,startangle=90,
        shadow=True ,explode=(0,0,0.1,0),
        autopct='1.5f%%')


plt.title('Pie Chart\n Check it out')
plt.show()
