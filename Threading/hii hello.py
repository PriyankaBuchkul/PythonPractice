import threading
import time

def f1():
      for i in range(5):
            print("Hi")
            time.sleep(2)

def f2():
      for i in range(5):
            print("Hello")
            time.sleep(2)

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
time.sleep(2)
t2.start()
t1.join()
t2.join()
            

