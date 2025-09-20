# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_sum=[0]*(len(s)+1)
        for start,end,direc in shifts:
            if direc==1:
                param=1
            else:
                param=-1

            pre_sum[start]+=param
            pre_sum[end+1]-=param
        sum=0
        # print(pre_sum)
        for i, val in enumerate(pre_sum):
            pre_sum[i]+=sum
            sum+=val
        # print(pre_sum)
        chars=ascii_lowercase
        d=defaultdict(int)
        for i,char in enumerate(chars):
            d[char]=i
        ans=[]
        for i,char in enumerate(s):
            new_idx=(d[char]+pre_sum[i])%26
            ans.append(chars[new_idx])
        return ''.join(ans)


        
