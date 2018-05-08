def addition(lis):
      sum=0
      if len(lis)>0:
            for i in lis:
                  if i>0:
                        sum=sum+i
            return sum
      else:
            return 0
           
print(addition([1,-4,8,12]))                 
                  
