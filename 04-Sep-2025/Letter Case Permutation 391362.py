# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def rec(st='' ,i=0):
            if i>=len(s):
                ans.append(st)
                return
            if not s[i].isdigit():
                rec(st+s[i].lower(),i+1)
                rec(st+s[i].upper(),i+1)
            else:
                rec(st+s[i],i+1)

        rec()
        return ans
        
        