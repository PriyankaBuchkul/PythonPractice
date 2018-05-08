class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self):
          for i in range(0,5):
                num=int(input("Please Enter the number:"))
                p=self.items.insert(0,num)
          print("The Entered Data is:",self.items)
        #self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q=Queue()
q.enqueue()
q.dequeue()

##q.enqueue('dog')
##q.enqueue(True)
##print(list(q.enqueqe()))
print(q.size())
#print(self.items)





















