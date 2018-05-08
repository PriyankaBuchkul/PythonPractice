#Name in a dictionary
d={'Name':[],'Age':[],'Salary':[]}


user=int(input("How many entries you want??"))

for i in range(user):
      d['Name'].append(input("please enter {} name :".format(i)))
      d['Age'].append(input("please enter {} Age :".format(i)))
      d['Salary'].append(input("please enter {} Salary :".format(i)))


print("dictionay is :",d)
