# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que=deque()
        que.append(root)
        turn=False
        while que:
            n=len(que)
            temp_arr=[]
            for _ in range(n):
                node=que.popleft()
                temp_arr.append(node)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if turn:
                a=0
                b=len(temp_arr)-1
                while a<b:
                    # print(temp_arr)
                    temp_arr[a].val,temp_arr[b].val=temp_arr[b].val,temp_arr[a].val
                    a+=1
                    b-=1
            turn=not turn
        return root
