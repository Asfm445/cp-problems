# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def oneTurn(self,turn_num,matrix,ans):
        i,j=turn_num,turn_num
        while j<len(matrix[0])-turn_num:
            ans.append(matrix[i][j])
            j+=1
        if turn_num==len(matrix)//2 or turn_num==j:
            return False
        i+=1
        while i<len(matrix)-turn_num:
            ans.append(matrix[i][j-1])
            i+=1
        if turn_num==len(matrix[0])//2:
            return False
        i-=1
        j-=1
        while j>turn_num:
            ans.append(matrix[i][j-1])
            j-=1
        i-=1
        if i==turn_num:
            return False
        while i>turn_num:
            ans.append(matrix[i][j])
            i-=1
        return True


    def spiralOrder(self, matrix):
        ans=[]
        turn=0
        while turn<=len(matrix)//2  and self.oneTurn(turn,matrix,ans):
            turn+=1
        return ans
        """
        :type matrix: List[List[int]]
        :rtype:
        """