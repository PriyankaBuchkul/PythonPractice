import threading
import time

def func():
      print("Start a thrad\n")
      time.sleep(6)
      print("End a thrad\n")
empty_list=[]

for i in range(10):
      print("First for loop is started ...")
      th=threading.Thread(target=func)#dont give brackets for function
      th.start()
      empty_list.append(th)
print("Threads:",empty_list)
for i  in empty_list:
      print("The Threas is :",i)
