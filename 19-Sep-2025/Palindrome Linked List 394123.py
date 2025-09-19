# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        cur=head
        c=0
        while cur:
            cur=cur.next
            c+=1
        if c%2==0:
            mid=c//2
        else:
            mid=c//2+1
        cur2=head
        li=[]
        # print(c,mid)
        for i in range(c):
            if i>=mid:
                # print(li[mid-(i+1-mid)])
                # print(cur2.data)
                if li[c-i-1]!=cur2.val:
                    return False
            else:
                li.append(cur2.val)
            cur2=cur2.next  
        else:
            return True
                