import sys
walked=[]
def bfs(M,now,canUp,r,c,MaxR,MaxC):
    #todo
    pass
t=1
for inp in sys.stdin:
    N,M=map(int,input().split())
    Map=[]
    for x in range(N):
        Map.append(list(map(int,input().split())))
    for x in range(M):
        print(x)
        if Map[0][x]==1:
            walked=[]
            bfs(Map,1,int(inp),0,x,N,M)
            break
    print(f"Case {t}:")
    ts=0
    for x in Map:
        for y in x:
            if ts!=0 and y==1:
                print(0,end=" ")
            else:
                print(y,end=" ")
        print()
        ts=1