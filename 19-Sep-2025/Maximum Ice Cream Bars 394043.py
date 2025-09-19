# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx=max(costs)
        counting_array=[0]*(mx+1)
        for cost in costs:
            counting_array[cost]+=1
        poss_cost=0
        ans=0
        i=1
        while i<=mx and poss_cost<coins:
            left=(coins-poss_cost)//i
            if left==0:
                break
            if counting_array[i]<=left:
                left=counting_array[i]
            poss_cost+=left*i
            ans+=left
            
            i+=1
        return ans
        