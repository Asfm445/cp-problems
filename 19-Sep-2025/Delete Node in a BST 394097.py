# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minleft(root):
            while root.left:
                root=root.left
            return root
        def rec(root,key):
            if not root:
                return None
            if key<root.val:
                root.left=rec(root.left,key)
            elif key>root.val:
                root.right= rec(root.right,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp=minleft(root.right)
                root.val=temp.val
                temp.val=key
                root.right=rec(root.right,key)
            return root
        return rec(root,key)
                


        