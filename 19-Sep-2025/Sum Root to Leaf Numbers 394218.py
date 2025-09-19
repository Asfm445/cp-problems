# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l=[]
        def rec(root,v=''):
            if not root:
                return
            if not root.left and not root.right:
                l.append(int(v+str(root.val)))
                return
            rec(root.left,v+str(root.val))
            rec(root.right,v+str(root.val))
        rec(root)
        return sum(l)
            

        