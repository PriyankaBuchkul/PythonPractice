import matplotlib.pyplot as plt

population_ages=[22,777,78,127,890,66,34,5,67,99,33,22,11,22,444,123,900,222,33,444,555,222,112,56,78]
print(len(population_ages))
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8,color='m')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting Graph \n Check it out')
plt.legend()
plt.show()
