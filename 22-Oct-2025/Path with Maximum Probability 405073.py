# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        for i in range(len(edges)):
            node1,node2=edges[i]
            graph[node1].append([node2,succProb[i]])
            graph[node2].append([node1,succProb[i]])
        

        heap=[]
        prob=[0]*n
        prob[start_node]=1
        heappush(heap,(-1,start_node))
        visited=set()
        while heap:
            node_prob,node=heappop(heap)
            node_prob*=-1
            # print(node_prob)
            if node==end_node:
                continue
            if node in visited:
                continue
            visited.add(node)
            for child,child_prob in graph[node]:
                cur_prob=node_prob*child_prob
                if prob[child]<cur_prob:
                    prob[child]=cur_prob
                    heappush(heap,(-cur_prob,child))
        return prob[end_node]


        