import threading
import time

class MyThread(threading.Thread):
      def run(self):
            print("{} started!".format(self.getName()))#thread x started
            time.sleep(1)                         #pretend to work for a second
            print("{} finished!".format(self.getName()))
if __name__=='__main__':
      for x in range(4):
            mythread=MyThread(name="Thread-{}".format(x + 1)) #instantiate a thread and pass 
            mythread.start()
            time.sleep(.9)


