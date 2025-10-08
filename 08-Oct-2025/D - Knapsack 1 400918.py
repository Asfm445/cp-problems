# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

n, W=map(int,input().split())

weight=[]
value=[]
for _ in range(n):
    wi,vi=map(int,input().split())

    weight.append(wi)
    value.append(vi)

dp=[[0]*(n+1) for _ in range(W+1)]


for w in range(1,W+1):
    # if w==W:
    #     print(dp)
    for i in range(1,n+1):
        if w >=weight[i-1]:
            # print(w-weight[i-1])
            # print(dp[w-weight[i-1]][i-1],value[i-1])
            dp[w][i]=max(dp[w][i-1], dp[w-weight[i-1]][i-1]+value[i-1])
        else:
            dp[w][i]=dp[w][i-1]

# print(dp)
print(max(dp[-1]))

