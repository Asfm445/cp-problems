# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(a,b,p1=0,p2=0,turn=True):
            if a>b:
                # print(p1,p2)
                return p1>=p2
            if turn:
                op1=rec(a+1,b,p1+nums[a],p2,False)
                op2=rec(a,b-1,p1+nums[b],p2,False)
                return op2 or op1
            else:
                op1=rec(a+1,b,p1,p2+nums[a],True)
                op2=rec(a,b-1,p1,p2+nums[b],True)
                return op1 and op2
        return rec(0,len(nums)-1)
        