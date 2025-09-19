# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class doubleLinkedList:
    def __init__(self):
        self.head=node()
        self.tail=node()
        self.head.next=self.tail
        self.tail.prev=self.head
    def append(self,node):
        temp=self.head.next
        node.next=temp
        temp.prev=node
        self.head.next=node
        node.prev=self.head
    def remove(self,node):
        temp=node.prev
        temp.next=node.next
        node.next.prev=temp
        return node
    def tofirst(self,node):
        self.append(self.remove(node))
    def pop(self):
        temp=self.tail.prev
        temp2=temp.prev
        temp2.next=self.tail
        self.tail.prev=temp2
        return temp
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.dll=doubleLinkedList()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.dll.tofirst(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value=value
            self.dll.tofirst(self.cache[key])
        else:
            n=node(key,value)
            self.dll.append(n)
            self.cache[key]=n
            if len(self.cache)>self.capacity:
                self.cache.pop(self.dll.pop().key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)