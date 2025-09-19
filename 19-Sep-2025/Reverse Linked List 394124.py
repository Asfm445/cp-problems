# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur=head
        f=cur
        cur=cur.next
        head=f
        f.next=None
        while cur:
            cur1=cur
            cur2=head
            cur=cur.next
            head=cur1
            cur1.next=cur2
        return head


        