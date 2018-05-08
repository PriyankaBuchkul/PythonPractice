import threading
import time

def Mytask():
      print("Hello World:{}".format(threading.current_thread()))
      print("Hello World:{}".format(threading.currentThread()))
my=threading.Thread(target=Mytask)
my.start()
