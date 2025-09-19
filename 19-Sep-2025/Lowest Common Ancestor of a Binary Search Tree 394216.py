# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root,p,q):
            if not root:
                return None
            if min(p.val,q.val)<=root.val and max(p.val,q.val)>=root.val:
                return root
            elif p.val<root.val:
                return func(root.left,p,q)
            elif p.val>root.val:
                return func(root.right,p,q)

            # return root
        return func(root,p,q)
        