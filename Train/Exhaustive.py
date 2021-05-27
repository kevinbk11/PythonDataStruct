import random as r
import time as T
test=[]
m,n,d=8,5,r.randrange(100)
for __ in range(m):
    l=[]
    for _ in range(n):
        l.append(r.randrange(-100,100))
    test.append(l)
for x in test:
    for y in x:
        print(y,end=" ")
    print()
ans=[]
global t
t=0
def bfs(m,r,c,walked,d,nowt):
    global t
    t+=1

    if (r,c) in walked:return
    if(r,c)==(len(m)-1,len(m[0])-1) and nowt+m[r][c]==d:
        walked.append((r,c))
        ans.append(walked)
        return
    n=walked.copy()
    n.append((r,c))
    if r+1<=len(m)-1:
        bfs(m,r+1,c,n,d,nowt+m[r][c])
    if c+1<=len(m[0])-1:
        bfs(m,r,c+1,n,d,nowt+m[r][c])
    if c-1>=0:
        bfs(m,r,c-1,n,d,nowt+m[r][c])
s=T.time()
bfs(test,0,0,[],d,0)
print(T.time()-s)
print(f"大小為{m}*{n}的矩形,從左上走到右下 且剛好數值為{d}的走法有:{len(ans)}種")
print("走法如下:")
for x in ans:
    print(x)
#複雜度太高
