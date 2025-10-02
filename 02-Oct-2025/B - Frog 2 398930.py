# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import math

n, k=map(int,input().split())

arr=list(map(int,input().split()))

dp=[0,math.fabs(arr[1]-arr[0])]

for i in range(2,len(arr)):
    mn=float("inf")
    for j in range(1,k+1):
        if i-j<0:
            break
        mn=min(mn,math.fabs(arr[i]-arr[i-j])+dp[-j])
    dp.append(mn)

print(int(dp[-1]))
# print(dp)