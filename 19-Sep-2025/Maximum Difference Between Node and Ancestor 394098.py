# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import *
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxm=[0]
        def rec(r,mi,ma=0):
            if not r:
                return None
            if r.val>ma:
                ma=r.val
            if r.val<mi:
                mi=r.val
            if abs(ma-r.val)>maxm[0]:
                maxm[0]=abs(ma-r.val)
            if abs(mi-r.val)>maxm[0]:
                maxm[0]=abs(mi-r.val)
            rec(r.left,mi,ma)
            rec(r.right,mi,ma)
        rec(root,root.val)
        return maxm[0]
        