# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph=[[float("inf")]*26 for i in range(26)]

        for i in range(len(original)):
            idx1=ord(original[i])-ord("a")
            idx2=ord(changed[i])-ord("a")
            graph[idx1][idx2]=min(cost[i],graph[idx1][idx2])

        for i in range(26):
            graph[i][i]=0

        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        ans=0
        for i in range(len(source)):
            i1=ord(source[i])-ord("a")
            i2=ord(target[i])-ord("a")
            if graph[i1][i2]<float("inf"):
                ans+=graph[i1][i2]
            else:
                return -1
        return ans

            
        