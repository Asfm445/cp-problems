# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

for _ in range(int(input())):
    s=input()
    let1=ord(s[0])-ord("a")+1
    let2=ord(s[1])-ord("a")+1

    if let2>let1:
        let2-=1

    ans= 25*(let1-1)+let2

    print(ans)