#merge to ductionary


d1={'a':2,'b':3,'c':6,'g':99}
d2={'a':7,'b':9,'c':7}

d1.update(d2)

z={**d1,**d2}  #update dictionary without using update
print(z)
