# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    n=int(input())
    if n&1:
        print(1 if n>2 else 3)
    else:
        num=1
        while not num & n:
            num<<=1
        print(num+1 if num==n else num)
        # print((i<<1)+1)
