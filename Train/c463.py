import sys
class node:
    def __init__(self,data):
        self.root=True
        self.value=data
        self.father=None
        self.child=[]
deepList=[]
def DFS(node,root):
    L=[]
    if node.child==[]:
        return 0
    for x in node.child:
        L.append(DFS(x,root)+1)
    deepList.append(max(L))
    if node.value==root.value:
        return sum(deepList)
    return max(L)
for Input in sys.stdin:
    basic=node(-1)
    tree=list((0 for x in range(int(Input)+1)))
    for x in range(1,int(Input)+1):
        data=list(map(int,(input().split())))
        list2=[]
        if type(tree[x])!=type(basic):
            tree[x]=node(x)
            for y in data[1:]:

                if type(tree[y])!=type(basic):
                    tree[y]=node(y)
                tree[y].father = x
                tree[x].child.append(tree[y])

        else :
            for y in data[1:]:
                if type(tree[y])!=type(basic):
                    tree[y]=node(y)
                tree[y].father=x
                tree[x].child.append(tree[y])

    '''for x in tree:
        if x!=0:
            for y in x.child:
              print(y.value,x.value)'''
    for y in tree:
        if y!=0:
            if y.father==None:
                print(y.value)
                root=y
                print(DFS(y,y))
                break
    deepList=[]