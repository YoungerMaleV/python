class Queue:
    def __init__(self):
        self.items=[]
 
    def enqueue(self,x):
        self.items.append(x)
 
    def dequeue(self):
        return self.items.pop(0)
 
    def size(self):
        return len(self.items)
 
    def isEmpty(self):
        return self.items==[]
    
    def get_items(self):
        return self.items
a=Queue()
b=int(input())
a.enqueue(9)
c=a.get_items()
while (c[0]%b!=0):
    a.enqueue(c[0]*10)
    a.enqueue(c[0]*10+9)
    a.dequeue()
print(c[0])
