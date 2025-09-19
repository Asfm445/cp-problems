# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=ListNode()
        l2=ListNode()
        h=l1
        h1=l2
        c=0
        cur=head
        while cur:
            if c%2==0:
                h.next=cur
                h=h.next
            else:
                h1.next=cur
                h1=h1.next
            # h=h.next
            # h1=h1.next
            cur=cur.next
            c+=1
        h1.next=None
        h.next=l2.next
        return l1.next
        
        