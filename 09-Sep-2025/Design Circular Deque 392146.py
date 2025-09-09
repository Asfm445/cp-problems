# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.que=[-1]*k
        self.rear=-1
        self.front=-1
        self.len=k
        

    def insertFront(self, value: int) -> bool:
        if self.que[self.front]==-1:
            self.que[self.front]=value
            self.front-=1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        temp=(self.rear+1)%self.len
        if self.que[temp]==-1:
            self.que[temp]=value
            self.rear=temp
            return True
        return False
        

    def deleteFront(self) -> bool:
        temp=(self.front+1)%self.len
        if self.que[temp]==-1:
            return False
        self.front=temp
        self.que[self.front]=-1
        return True
        
        

    def deleteLast(self) -> bool:
        if self.que[self.rear]!=-1:
            self.que[self.rear]=-1
            self.rear-=1
            return True
        return False
        
        

    def getFront(self) -> int:
        temp=(self.front+1)%self.len
        return self.que[temp] 
        

    def getRear(self) -> int:
        return self.que[self.rear] 
        

    def isEmpty(self) -> bool:
        temp=(self.front+1)%self.len
        return True if self.que[temp]==-1 else False
        

    def isFull(self) -> bool:
        temp=(self.rear+1)%self.len
        return True if self.que[temp]>-1 else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()