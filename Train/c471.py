#c471

import sys
class item:
    def __init__(self,weight,times,number):
        self.w=weight
        self.t=times
        self.n=number
for x in sys.stdin:
    x=int(x)
    weight=list(map(int,input().split()))
    times=list(map(int,input().split()))
    l=[]
    all=0
    for a in range(x):
        l.append(item(weight[a],times[a],a+1))
    for i in range(0,x-1):
        for j in range(x-1,i,-1):
            if l[i].w*l[j].t>l[j].w*l[i].t:#0 1,1 0

                l[i],l[j]=l[j],l[i]
    s=0
    r=0
    for y in range(0,x-1):
        s+=l[y].w
        r+=s*l[y+1].t
    print(r)
