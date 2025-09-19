# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.head=node()
    def get(self, index: int) -> int:
        cur=self.head
        if cur.next:
            cur=cur.next
        else:
            return -1
        a=0
        while a<index:
            if cur.next:
                cur=cur.next
            else:
                return -1
            a+=1
        return cur.val
    def addAtHead(self, val: int) -> None:
        n=node(val)
        cur=self.head
        cur1=cur.next
        cur.next=n
        n.next=cur1
    def addAtTail(self, val: int) -> None:
        cur=self.head
        while cur.next:
            cur=cur.next
        n=node(val)
        cur.next=n
    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.head
        for i in range(index):
            if cur.next:
                cur=cur.next
            else:
                return None
        if cur.next:
            cur1=cur.next
        else:
            cur1=None
        n=node(val)
        cur.next=n
        n.next=cur1
    def deleteAtIndex(self, index: int) -> None:
        cur=self.head
        if cur.next:
            cur1=cur.next
        else:
            return None
        for i in range(index):
            if cur1.next:
                cur1=cur1.next
            else:
                return None
            cur=cur.next
        if cur1.next:
            cur2=cur1.next
        else:
            cur2=None
        cur.next=cur2
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# # obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)