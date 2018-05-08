import matplotlib.pyplot
f=open("Demo.txt",'w+')
for i in matplotlib.style.available:
      f.write(i+'\n')
      print(i)

f.close()
