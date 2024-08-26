n=int(input())
ans=[0 for _ in range(n)]
for i in range(n):
    ans[int(input())-1]+=1
ans2 = -1
ans0 = -1
for i in range(n):
    if ans[i]==2:
        ans2 = i+1
    elif ans[i]==0:
        ans0 = i+1
if ans2==-1:
    print('Correct')
else:
    print(ans2,ans0)
