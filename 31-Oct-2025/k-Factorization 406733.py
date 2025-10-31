# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

n, k= map(int,input().split())

d=2
pr=[]

while d*d<=n:
    while n%d==0:
        pr.append(d)
        n//=d
    d+=1

if n>1:
    pr.append(n)

# print(pr)
n=len(pr)


if n<k:
    print(-1)
else:
    while n>k:
        p=pr.pop()
        pr[-1]*=p
        n-=1
    print(*pr)
