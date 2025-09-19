# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        d=dummy
        d.next=head
        if not head:
            return None
        slow=d.next
        if head.next:
            fast=d.next
        else:
            return None
        while fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            if fast==slow:
                break
        else:
            return None
        slow=d.next
        while fast!=slow:
            if fast.next:
                fast=fast.next
            else:
                return None
            slow=slow.next
        return slow

        