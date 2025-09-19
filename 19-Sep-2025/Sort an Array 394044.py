# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def marge(x,y):
            a=0
            b=0
            l=[]
            while a<len(x) and b<len(y):
                if x[a]<=y[b]:
                    l.append(x[a])
                    a+=1
                elif x[a]>y[b]:
                    l.append(y[b])
                    b+=1
            l.extend(x[a:])
            l.extend(y[b:])
            return l
        def rec(arr):
            if not arr:
                return []
            if len(arr)==1:
                return arr
            m=len(arr)//2
            left=rec(arr[:m])
            right=rec(arr[m:len(arr)])

            return marge(left,right)
        return rec(nums)
                    