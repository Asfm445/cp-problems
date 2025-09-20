# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls=[homepage]
        self.ptr=0
        

    def visit(self, url: str) -> None:
        while len(self.urls)-1>self.ptr:
            self.urls.pop()
        self.urls.append(url)
        self.ptr+=1
    def back(self, steps: int) -> str:
        if steps>self.ptr:
            self.ptr=0
            return self.urls[0]
        self.ptr-=steps
        return self.urls[self.ptr]
        

    def forward(self, steps: int) -> str:
        if steps+self.ptr>=len(self.urls):
            self.ptr=len(self.urls)-1
            return self.urls[self.ptr]
        self.ptr+=steps
        return self.urls[self.ptr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)