# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def marge(h1,h2):
            n=ListNode()
            d=n
            while h1 and h2:
                if h1.val<=h2.val:
                    d.next=h1
                    h1=h1.next
                else:
                    d.next=h2
                    h2=h2.next
                d=d.next
            while h1:
                d.next=h1
                h1=h1.next
                d=d.next
            while h2:
                d.next=h2
                h2=h2.next
                d=d.next
            return n.next
        def div(h):
            slow=h
            fast=h
            s=slow
            while fast and  fast.next:
                s=slow
                slow=slow.next
                fast=fast.next.next
            s.next=None
            return slow
        def rec(head):
            if not head:
                return None
            if not head.next:
                return head
            m=div(head)
            left=rec(head)
            right=rec(m)
            return marge(left,right)
        return rec(head)
        