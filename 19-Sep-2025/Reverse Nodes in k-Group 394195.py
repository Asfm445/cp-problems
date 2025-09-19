# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        d=dummy
        def rec(head, num=1):
            # print(head)
            if not head:
                return None,None
            if num==k:
                # print(head)
                d.next=head
                return head, head.next
            h1,h2=rec(head.next,num+1)
            if h1:
                h1.next=head
                head.next=h2
                return head, h2
            return None,None
        while d:
            h1, head=rec(head)
            d=h1
        return dummy.next
        


                



            
        