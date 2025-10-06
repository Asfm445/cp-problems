# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

num=int(input())

ans=0


for n in range(2,num+1):
    # print(n, end=" ")
    cur=n
    s=set()
    d=2
    while d*d<=n:
        while n%d==0:
            s.add(d)
            n//=d
        d+=1
        if len(s)>2:
            break
    if n>1:
        s.add(n)

    # print(s)
    if len(s)==2:
        # print(cur, s)
        ans+=1

print(ans)