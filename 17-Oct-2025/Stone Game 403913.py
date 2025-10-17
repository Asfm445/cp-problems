# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo={}

        def rec(i,j, turn):
            if i>=j:
                return 0,0
            if (i,j,turn) not in memo:
                op1_val1,op1_val2=rec(i+1,j, not turn)
                op2_val1,op2_val2=rec(i,j-1, not turn)
                op1_val1+=piles[i]
                op2_val1+=piles[j]
                if turn:
                    if op1_val1-op1_val2>=op2_val1-op2_val2:
                        memo[(i,j,turn)]= op1_val1, op1_val2
                    else:
                        memo[(i,j,turn)]=op2_val1, op2_val2
                else:
                
                    if op1_val1-op1_val2>=op2_val1-op2_val2:
                        memo[(i,j,turn)]=op2_val1, op2_val2
                    else:
                        memo[(i,j,turn)]=op1_val1, op1_val2
            return memo[(i,j,turn)]
        ans=rec(0,len(piles)-1,True)
        return ans[0]>ans[1]
            
        