# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        dummy=ListNode()
        d=dummy
        d.next=head
        a=0
        while cur:
            cur=cur.next
            a+=1
        print(a)
        cur=head
        for i in range(a-n):
            d=d.next
            cur=cur.next
        if cur.next:
            cur1=cur.next
        else:
            cur1=None
        d.next=cur1
        return dummy.next
        