import sys
sys.setrecursionlimit(100000)

class task:
    def __init__(self, name, money, time):
        self.Name = name
        self.Money = money
        self.Time = time
ans=[]
def dp(List,n,nowW,maxW,DP):
    global ttt
    ttt+=1
    if n==0:
        return 0
    if DP[n][nowW]!=-1:
        return DP[n][nowW]
    else:
        a=0
        if nowW+List[0].Time<=maxW:
            a=dp(List[1:],len(List[1:]),nowW+List[0].Time,maxW,DP)+List[0].Money
        b=dp(List[1:],len(List[1:]),nowW,maxW,DP)
        DP[n][nowW]=max(a,b)
        return DP[n][nowW]
for inp in sys.stdin:
    Task = []
    T, N = map(int, inp.split())
    Max = -1
    name=""
    DP=list(list(-1 for x in range(T+1)) for y in range(N+1)) # 選到第A項 目前重量還有B
    for _ in range(N):
        t = list(input().split())
        if int(t[1]) // int(t[2]) > Max:
            Max = int(t[1]) // int(t[2])
            name=t[0]
        Task.append(task(t[0], int(t[1]), int(t[2])))
    global ttt
    ttt=0

    dp(Task,len(Task),0,T,DP)
    print(ttt)
    print(max(DP[-1]))
    print(name)