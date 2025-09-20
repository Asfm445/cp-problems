# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum=0
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.bstToGst(root.right)
        self.sum+=root.val
        root.val=self.sum
        self.bstToGst(root.left)

        return root
        
        