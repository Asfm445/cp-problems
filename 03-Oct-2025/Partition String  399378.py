# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        hash_set=set()
        st=''
        ans=[]
        for i in s:
            conc=st+i
            if conc in hash_set:
                st=conc
            else:
                hash_set.add(conc)
                ans.append(conc)
                st=""
            # print(hash_set)
        return ans
        