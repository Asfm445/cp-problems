# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

for _ in range(int(input())):
    l,r,d=map(int,input().split())

    if l>d:
        print(d)
    else:
        md=r%d
        print(r+d-md)