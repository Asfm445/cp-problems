# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.l=[]
        

    def push(self, x: int) -> None:
        self.l.append(x)
        return 
        

    def pop(self) -> int:
        if self.l:
            return self.l.pop()
        

    def top(self) -> int:
        if self.l:
            return self.l[-1]
        

    def empty(self) -> bool:
        if self.l:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()