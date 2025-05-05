# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def rec(root,val):
            if not root:
                return True
            if root.val!=val:
                return False
            left=rec(root.left,val)
            right=rec(root.right,val)
            
            return left and right
        return rec(root,root.val)