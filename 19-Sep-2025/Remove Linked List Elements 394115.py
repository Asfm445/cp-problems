# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        n=ListNode()
        n.next=head
        cur=head
        cur1=n
        while cur:
            cur2=None
            if cur.next:
                cur2=cur.next
            if cur.val==val:
                cur1.next=cur2
            else:
                cur1=cur1.next
            cur=cur2
            
        

        
        return n.next

        