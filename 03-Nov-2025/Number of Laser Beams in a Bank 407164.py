# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        back=bank[0].count("1")
        ans=0
        for i in range(1,len(bank)):
            cur=bank[i].count("1")
            ans+=back*cur
            # print(back,ans,cur)
            if cur>0:
                back=cur
        return ans
        