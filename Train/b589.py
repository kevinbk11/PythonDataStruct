import sys
dp=[]
def go(road,flag,n):
    if road==[]:return 0
    if flag==True:
        norun=go(road[1:],False,n+1)
        return norun
    else:
        if dp[n]==0:
            run=go(road[1:],True,n+1)+road[0]*2
            norun=go(road[1:],False,n+1)+road[0]
            dp[n]=max(run,norun)
            return max(run,norun)
        else:
            return dp[n]
for inp in sys.stdin:
    if int(inp)==0:break
    road=list(map(int,input().split()))
    dp=[0 for x in range(len(road)+1)]
    print(go(road,False,1))
