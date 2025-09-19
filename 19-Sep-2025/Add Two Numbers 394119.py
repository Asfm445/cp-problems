# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode()
        head=l
        v=0
        while l1 or l2:
            if l1 and l2:
                n=ListNode()
                c=(v+l1.val+l2.val)%10
                v=(v+l1.val+l2.val)//10
                n.val=c
                head.next=n
                l1=l1.next
                l2=l2.next
            elif l1:
                n=ListNode()
                c=(v+l1.val)%10
                v=(v+l1.val)//10
                n.val=c
                head.next=n
                l1=l1.next
            elif l2:
                n=ListNode()
                c=(v+l2.val)%10
                v=(v+l2.val)//10
                n.val=c
                head.next=n
                l2=l2.next
            head=head.next
        else:
            if v>0:
                n=ListNode()
                n.val=v
                head.next=n
        return l.next

            


        

        