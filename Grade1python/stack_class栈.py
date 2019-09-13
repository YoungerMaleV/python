class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
a=input()
zhan=Stack()
biao=list(a)
b=1
for c in biao:
    if c =='}' or c ==')' or c ==']':
        if zhan.isEmpty():
            b=2
        elif c =='}' and zhan.peek()!= '{':
            b=2
        elif c ==')' and zhan.peek()!='(':
            b=2
        elif c ==']' and zhan.peek()!='[':
            b=2
        else:
            zhan.pop()
    else :
        zhan.push(c)
if zhan.isEmpty() and b==1:
    print('True')
else :
    print('False')
    
