# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def rec(root):
            if not root:
                return 0,0,0
            left_sum, left_num, left_ans=rec(root.left)
            right_sum, right_num, right_ans=rec(root.right)
            cur_ans=left_ans+right_ans
            cur_sum=left_sum+right_sum+root.val
            cur_num=left_num+right_num+1
            if (cur_sum)//(cur_num)==root.val:
                cur_ans+=1
            

            return cur_sum,cur_num, cur_ans
        return rec(root)[2]




        