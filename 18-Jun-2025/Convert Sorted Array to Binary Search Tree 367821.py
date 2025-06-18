# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def rec(arr):
            if not arr:
                return None

            if len(arr)==1:
                return TreeNode(arr[0])
            m=len(arr)//2
            root=TreeNode(arr[m])
            root.left=rec(arr[:m])
            root.right=rec(arr[m+1:])

            return root
        return rec(nums)
        