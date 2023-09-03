import sys

sys.stdin = open("input.txt")

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self,N):
        self.stack.append(N)
    
    def pop(self):
        pop_object = None
        if self.isEmpty():
            # print("stack is Empty!!")
            pop_object = -1
        else:
            pop_object = self.stack.pop()
        
        return pop_object
    
    def top(self):
        top_object = None
        if self.isEmpty():
            # print("stack is Empty!!")
            top_object = -1
        else:
            top_object = self.stack[-1]
        
        return top_object
    
    def size(self):
        size_object = None
        if self.isEmpty():
            # print("stack is Empty!!")
            size_object = 0
        else:
            size_object = len(self.stack)
        return size_object
        
    def isEmpty(self):
        Is_Empty = 0
        if len(self.stack) == 0:
            Is_Empty = 1
        
        return Is_Empty
    
N = int(sys.stdin.readline())
stack = Stack()
for i in range(N):
    com = sys.stdin.readline()
    com2 = com[:3]
    if com2 == "pus":
        stack.push(int(com[5:]))
        continue
    if com2 == "top":
        print(stack.top())
    if com2 == "pop":
        print(stack.pop())
    if com2 == "siz":
        print(stack.size())
    if com2 == "emp":
        print(stack.isEmpty())
    
