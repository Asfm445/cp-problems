# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que=deque()
        que.append(root)
        ans=[]
        while que:
            ans.append([])
            for i in range(len(que)):
                p=que.popleft()
                ans[-1].append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
        return ans

        