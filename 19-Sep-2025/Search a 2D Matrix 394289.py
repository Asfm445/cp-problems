# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl=0
        rr=len(matrix)-1
        cl=0
        cr=len(matrix[0])-1
        while rl<=rr:
            rm=rl+(rr-rl)//2
            while cl<=cr:
                cm=cl+(cr-cl)//2
                if matrix[rm][cm]>target:
                    cr=cm-1
                elif matrix[rm][cm]<target:
                    cl=cm+1
                else:
                    return True
            else:
                if matrix[rm][cm]>target:
                    rr=rm-1
                elif matrix[rm][cm]<target:
                    rl=rm+1
                cl=0
                cr=len(matrix[0])-1
        return False