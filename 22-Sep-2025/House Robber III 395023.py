# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def rec(root,state=True):
            if not root:
                return 0
            if not state:
                return rec(root.left)+rec(root.right)
            if root not in memo:
                memo[root]=max(root.val+rec(root.left, state=False)+rec(root.right, state=False),rec(root.left)+rec(root.right))
            return memo[root]

        return rec(root)
        