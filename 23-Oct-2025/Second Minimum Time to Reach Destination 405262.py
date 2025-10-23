# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

from collections import deque, defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize distance arrays for shortest and second shortest
        shortest = [float('inf')] * (n + 1)
        second_shortest = [float('inf')] * (n + 1)
        shortest[1] = 0
        que = deque([(1, 0)])
        
        while que:
            node, current_time = que.popleft()
            for neighbor in graph[node]:
                # Calculate the new time after traversing the edge
                # Determine if we need to wait at the traffic light
                total_time = current_time
                # Check if the traffic light is red
                if (total_time // change) % 2 == 1:
                    # Wait until the next green light
                    total_time += change - (total_time % change)
                total_time += time
                
                # Update the shortest and second shortest times for the neighbor
                if total_time < shortest[neighbor]:
                    second_shortest[neighbor] = shortest[neighbor]
                    shortest[neighbor] = total_time
                    que.append((neighbor, total_time))
                elif shortest[neighbor] < total_time < second_shortest[neighbor]:
                    second_shortest[neighbor] = total_time
                    que.append((neighbor, total_time))
        
        return second_shortest[n]
        
        