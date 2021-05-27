import sys
class node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.right=None
        self.left=None
class tree:
    def __init__(self,start,end):
        self.node=node(start,end)
        self.s=0
    def addNewRange(self,point,now):
        if (point>=now.start and point<=now.end) and now.left!=None:
            if point>now.left.end:
                self.addNewRange(point,now.right)
            else:
                self.addNewRange(point,now.left)

        elif (point>=now.start and point<=now.end) and now.left==None:
            self.s+=now.end-now.start
            now.left=node(now.start,point)
            now.right=node(point,now.end)
        elif point>now.end or point<now.start:
            return
    def a(self,now):
        if now==None:return 0
        if now.left==None:return 0
        L=self.a(now.left)
        R=self.a(now.right)
        s=now.end-now.start
        return L+R+s
class cut:
    def __init__(self,point,f):
        self.p=point
        self.f=f
for inp in sys.stdin:
    a,b=map(int,inp.split())
    l=[]
    r=tree(0,b)
    for x in range(a):
        p,f=map(int,input().split())
        l.append(cut(p,f))
    l.sort(key=lambda x:x.f)
    for x in l:
        r.addNewRange(x.p,r.node)
    print(r.s)A
