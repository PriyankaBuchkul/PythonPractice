total=0
cnt=0
avg=0

while True:
      n= input("Enter Any number:")
      if n == "done":
            break
      else:
            try:
                  total += int(n)
                  cnt += 1
                  avg = total / cnt
            except ValueError as ex:
                  print("Invalid Input:")
                  print('"%s" cannot be converted into int :%s'%(n,ex))
print("Total is {} and count is {} ,Average of numbers is:{}".format(total,cnt,avg))
