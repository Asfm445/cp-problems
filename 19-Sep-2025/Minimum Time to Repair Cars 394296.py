# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left=1
        right=min(ranks)*cars*cars
        def check(md):
            count=0
            for i in ranks:
                temp=sqrt(md/i)
                count+=int(temp)
            if count>=cars:
                # print(count,md)
                return True
            return False
        # print(left,right)
        while left<=right:
            md=left+(right-left)//2
            if check(md):
                right=md-1
            else:
                left=md+1
        # print(check(left))
        return left
        