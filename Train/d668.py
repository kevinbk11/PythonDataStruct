class SegmentNode:
    def __init__(self, rg):
        self.range = rg
        self.max = None
        self.min = None
        self.r = None
        self.l = None
        self.s=None
        self.e=None
class SegmentTree:
    def __init__(self, data):
        self.top = SegmentNode(data)
        self.build(self.top, True)

    def build(self, data, first):
        if len(data.range) == 1: return data.range[0], data.range[0]
        if first:
            self.top.s=1
            self.top.e=len(data.range)

            self.top.l = SegmentNode(data.range[0:len(data.range) // 2])
            self.top.l.s=1
            self.top.l.e=len(data.range)//2

            self.top.r = SegmentNode(data.range[len(data.range) // 2:len(data.range)])
            self.top.r.s=len(data.range)//2+1
            self.top.r.e=len(data.range)

            m1, n1 = self.build(self.top.l, False)
            m2, n2 = self.build(self.top.r, False)

            self.top.max = max(m1, m2)
            self.top.min = min(n1, n2)

        else:
            data.l = SegmentNode(data.range[0:len(data.range) // 2])
            if len(data.l.range)==1:
                data.l.s=data.s
                data.l.e=data.s
            else:
                data.l.s=data.s
                data.l.e=data.s+len(data.range)//2-1
            data.l.mid=(data.l.s+data.l.e)//2
            data.r = SegmentNode(data.range[len(data.range) // 2:len(data.range)])
            if len(data.r.range)!=1:
                data.r.s=data.l.e+1
                data.r.e=data.e
            else:
                data.r.s = data.l.e + 1
                data.r.e=data.r.s
            data.r.mid=(data.r.s+data.r.e)//2
            m1, n1 = self.build(data.l, False)
            m2, n2 = self.build(data.r, False)
            data.max = max(m1, m2)
            data.min = min(n1, n2)
            return data.max, data.min

    def printAll(self, nd):
        if nd == None: return
        print(nd.range,nd.max,nd.min,nd.s,nd.e)
        self.printAll(nd.l)
        self.printAll(nd.r)
    def searchRange(self,nd,start,end):
        if len(nd.range)==1 or nd.s==nd.e:
            return nd.range[0],nd.range[0]
        if nd.s>=start and nd.e<=end:
            return nd.max,nd.min
        if start<=nd.l.e and end >=nd.r.s:
            m1,n1=self.searchRange(nd.l,start,end)
            m2,n2=self.searchRange(nd.r,start,end)


            return max(m1,m2),min(n1,n2)
        elif (start>=nd.l.s and end<=nd.l.e) or (start>=nd.r.s and end>=nd.r.e):
            m1,n1=self.searchRange(nd.l,start,end)
            return m1,n1
        elif (start>=nd.r.s and end<=nd.r.e) or (start<=nd.l.s and end>=nd.l.s):
            m1,n1=self.searchRange(nd.r,start,end)
            return m1,n1
import sys
import random as r
for inp in sys.stdin:
    N,Q=map(int,inp.split())
    l=[x for x in range(6)]
    r.shuffle(l)
    root=SegmentTree(l)
    root.printAll(root.top)
    print(root.searchRange(root.top,1,5))
    '''l=[]
    for x in range(N):
        d=int(input())
        l.append(d)
    root=SegmentTree(l)
    for x in range(Q):
        start,end=map(int,input().split())
        if start==end:
            print(0)
        else:
            m,n=root.searchRange(root.top,start,end)
            print(m-n)'''