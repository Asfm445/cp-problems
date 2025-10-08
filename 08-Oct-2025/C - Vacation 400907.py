# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

n=int(input())


x,y,z=0,0,0
s1,s2,s3=0,0,0
for _ in range(n):
    a,b,c=map(int,input().split())
    s1=a+max(y,z)
    s2=b+max(x,z)
    s3=c+max(x,y)

    x,y,z=s1,s2,s3
    
print(max(x,y,z))