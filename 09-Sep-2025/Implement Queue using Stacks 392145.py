# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

from collections import *
class MyQueue:

    def __init__(self):
        self.l=deque()
        

    def push(self, x: int) -> None:
        self.l.appendleft(x)
        

    def pop(self) -> int:
        return self.l.pop()
        

    def peek(self) -> int:
        return self.l[-1]
        

    def empty(self) -> bool:
        if self.l:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()