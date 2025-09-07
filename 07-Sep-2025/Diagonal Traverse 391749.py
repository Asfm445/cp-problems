# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/



class Solution(object):
    def inBound(self,x,y,matrix):
        return 0<=x<len(matrix) and 0<=y<len(matrix[0])
    def traverse(self,turn,mat,ans,i=0,j=0):
        # print(i,j)
        if turn:
            dir=(-1,1)
        else:
            dir=(1,-1)
        while self.inBound(i,j,mat):
            ans.append(mat[i][j])
            i+=dir[0]
            j+=dir[1]
        return i,j
        

    def findDiagonalOrder(self, mat):
        turn=True
        i=0
        j=0
        ans=[]
        while 0<=i<len(mat) and 0<=j<len(mat[0]):
            i,j=self.traverse(turn,mat,ans,i,j)
            if turn:
                if j>=len(mat[0]):
                    i+=2
                    j-=1
                else:
                    i+=1
            else:
                if i>=len(mat):
                    j+=2
                    i-=1
                else:
                    j+=1
            turn=not turn
        return ans
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

