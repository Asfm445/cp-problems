# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/


class RecentCounter:

    def __init__(self):
        self.que=[]
        self.rear=0
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        while min(t-3000,t)>self.que[self.rear]:
            self.rear+=1
        return len(self.que)-self.rear


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)