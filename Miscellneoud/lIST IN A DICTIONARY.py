d={'hello':[{'channel':[{'episode':[{'a':1,'b':2}]}]}]}

for i in d.values():
      for j in i:
            for k in j.values():
                  for l in k:
                        print(l.values())


myList =[ [(' whether', None), (' mated', None), (' rooster', None), ('', None)] ,
          [(' produced', None), (' without', None), (' rooster', None), (' infertile', None), ('', None)] ]

print [[x[1] for x in el for el in myList]
