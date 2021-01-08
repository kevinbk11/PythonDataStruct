import sys
t=1
for inp in sys.stdin:
    N,M=map(int,inp.split())
    l=[]
    for x in range(N):
        i=list(map(int,input().split()))
        l.append(i)
    dp=list(list(0 for x in range(M))for y in range(N))
    dp[0][0]=l[0][0]
    for x in range(1,M):
        dp[0][x]=dp[0][x-1]+l[0][x]
    for y in range(1,N):
        dp[y][0]=dp[y-1][0]+l[y][0]
    for x in range(1,N):
        for y in range(1,M):
            dp[x][y]=min(dp[x-1][y]+l[x][y],dp[x][y-1]+l[x][y])
    print(f"Case #{t}")
    t+=1
    print(dp[-1][-1])