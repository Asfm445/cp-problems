# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        def rec(root,ptr=0):
            if not root:
                return None
            if ptr>=len(l):
                l.append([])
            l[ptr].append(root.val)
            rec(root.left,ptr+1)
            rec(root.right,ptr+1)

        rec(root)
        return l
        