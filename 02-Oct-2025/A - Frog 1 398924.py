# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import math

n=int(input())

arr=list(map(int,input().split()))

dp=[0,math.fabs(arr[1]-arr[0])]

for i in range(2,len(arr)):
    dp.append(min(math.fabs(arr[i]-arr[i-1])+dp[-1],math.fabs(arr[i]-arr[i-2])+dp[-2]))

print(int(dp[-1]))
# print(dp)