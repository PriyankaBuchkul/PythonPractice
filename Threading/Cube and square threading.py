import threading
import time

def square(num):
      print("Calculate Square Numbaer\n")
      for n in num:
            time.sleep(2)
            print("square is:",n*n)

def cube(num):
      print("Calculate Cube Numbaer\n")
      for n in num:
            time.sleep(2)
            print("Cube is:",n*n*n)

arr=[2,3,8,9]

t=time.time()
t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))


t1.start()
t2.start()

print("Done In:",time.time()-t)
print("haaa.. I am done with all my work now ...!!")
      
