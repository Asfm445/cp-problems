# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import  deque
n, m=map(int,input().split())


railway=[[0 for _ in range(n+1)] for _ in range(n+1)]
road=[[1 for _ in range(n+1)]for _ in range(n+1)]

# print(road, railway)
# print(railway)

for _ in range(m):
    a,b=map(int,input().split())
    railway[a][b]=1
    railway[b][a]=1
    road[a][b]=0
    road[b][a]=0
    # print(railway,a,b, railway[a][b])



def bfs(graph):
    dis=[float("inf")]*(n+1)
    que=deque()
    que.append((1,0))
    while que:
        node, node_dis=que.popleft()

        for i in range(1,n+1):
            if graph[node][i]==1 and dis[i]>node_dis+1:
                dis[i]=node_dis+1
                que.append((i,node_dis+1))

    return dis[n] if dis[n]<float("inf") else -1

ans1=bfs(railway)
ans2=bfs(road)
# print(road, railway)
# print(railway)
# print(ans1,ans2)
if ans1 == -1 or ans2 == -1:
    print(-1)
else:
    print(max(ans1, ans2))


    


    


