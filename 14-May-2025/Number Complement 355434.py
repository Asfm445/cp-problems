# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        while (1<<i)<=num:
            num^=(1<<i)
            i+=1
        return num