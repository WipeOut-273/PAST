n=int(input())
now=int(input())
for i in range(n-1):
    A=int(input())
    ans=''
    if A>now:
        ans='up'
        print(ans, A-now)
        now=A
    elif A<now:
        ans='down'
        print(ans, now-A)
        now=A
    else:
        print('stay')