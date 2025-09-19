# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.l=[]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        def rec(root,ptr):
            if not root:
                return 
            if len(l)<=ptr:
                l.append([])
            l[ptr].append(root.val)
            rec(root.left,ptr+1)
            rec(root.right,ptr+1)
        rec(root,0)
        for i in range(len(l)):
            if i%2==1:
                l[i]=l[i][::-1]
        return l
        