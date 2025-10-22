# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=int(1e9)+7

        graph=defaultdict(list)
        time=[float("inf")]*n
        num_ways=[1]*n

        for node1,node2,timei in roads:
            graph[node1].append([node2,timei])
            graph[node2].append([node1,timei])

        heap=[(0,0)]
        # print(graph)
        # print(time)
        time[0]=0
        visited=[False]*n
        while heap:
            node_time,node=heappop(heap)
            # print(node_time,node)
            # print(visited[node])
            if visited[node]:
                continue
            visited[node]=True
            if node==n-1:
                continue
            # print(graph[node])

            for child,child_time in graph[node]:
                cur_time=node_time+child_time
                # print(cur_time<time[child],cur_time,time[child])
                if cur_time<time[child]:
                    time[child]=cur_time
                    heappush(heap,(cur_time,child))
                    num_ways[child]=num_ways[node]%mod
                elif cur_time==time[child]:
                    num_ways[child]+=(num_ways[node])%mod
            # print(num_ways,time,node)

        # print(num_ways, time)
        return num_ways[n-1]%mod
        
                    
                
        
        