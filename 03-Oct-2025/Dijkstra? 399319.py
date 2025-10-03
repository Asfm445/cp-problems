# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import heapq
import sys

def main():
    # Read input efficiently
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    
    # Optimized graph representation using list of lists
    graph = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        n1, n2, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))
    
    # Memory optimization: use single list for both distance and visited tracking
    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    # Backtracking array
    prev = [0] * (n + 1)  # Use 0 instead of None for smaller memory
    
    # Priority queue
    heap = [(0, 1)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        # Skip if we found a better path already
        if current_dist > dist[node]:
            continue
            
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    
    # Reconstruct path
    if dist[n] == INF:
        print(-1)
        return
        
    path = []
    current = n
    while current != 0:  # Changed from None to 0
        path.append(current)
        current = prev[current]
    
    if path[-1] == 1:
        print(' '.join(map(str, path[::-1])))
    else:
        print(-1)

main()