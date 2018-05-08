def permute(n,i):
      if i == len(n)-1:
            print(n)
      else:
            for j in range(i,len(n)):
                  n[i],n[j] =
                  n[j],n[i]
                  permute(n,i+1)
                  n[i],n[j] = n[j],n[i]



permute([1,2,3],0)
