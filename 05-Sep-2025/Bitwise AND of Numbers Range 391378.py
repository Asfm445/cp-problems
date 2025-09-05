# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        pt=31
        ans=0
        while pt>=0:
            if 1<<pt&right and 1<<pt & left:
                ans+=1<<pt
                pt-=1
            elif not 1<<pt&right and not 1<<pt & left:
                pt-=1
            else:
                break
        return ans
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        