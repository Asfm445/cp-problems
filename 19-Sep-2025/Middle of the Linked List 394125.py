# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        c=0
        while cur:
            c+=1
            cur=cur.next
        if c%2==0:
            m=c//2
        else:
            m=c//2
        cur1=head
        c1=0
        while cur1:
            if c1==m:
                print(c)
                return cur1
            cur1=cur1.next
            c1+=1

        