# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

import math
n,m=map(int,input().split())

mn=math.ceil(n/2)
for i in range(mn, n+1):
    if i%m==0:
        print(i)
        break
else:
    print(-1)