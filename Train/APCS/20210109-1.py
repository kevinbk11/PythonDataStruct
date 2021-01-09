import sys
for inp in sys.stdin:
    n,d=map(int,inp.split())
    s=0
    buyTimes=0
    for _ in range(n):
        ItemCount=list(map(int,input().split()))
        x=max(ItemCount)-min(ItemCount)
        if x>=d:
            buyTimes+=1
            s+=sum(ItemCount)//3
    print(buyTimes,s)