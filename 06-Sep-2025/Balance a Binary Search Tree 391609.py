# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def traverse(self,node):
        if not node:
            return []
        left=self.traverse(node.left)
        right=self.traverse(node.right)
        return left+[node.val]+right
    def build(self,arr):
        if not arr:
            return None
        m=len(arr)//2
        left=self.build(arr[:m])
        right=self.build(arr[m+1:])

        return TreeNode(arr[m],left,right)
    def balanceBST(self, root):
        arr=self.traverse(root)
        return self.build(arr)
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        