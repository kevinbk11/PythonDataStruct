class SegmentNode:
    def __init__(self,rg):
        self.range=rg
        self.max=None
        self.min=None
        self.r=None
        self.l=None
class SegmentTree:
    def __init__(self,data):
        self.top=node(data)
        self.build(self.top,True)
    def build(self,data,first):
        
        if len(data.range)==1:return data.range[0],data.range[0]
        if first:
            self.top.l=SegmentNode(data.range[0:len(data.range)//2])
            self.top.r=SegmentNode(data.range[len(data.range)//2:len(data.range)])
            m1,n1=self.build(self.top.l,False)
            m2,n2=self.build(self.top.r,False)
            self.top.max=max(m1,m2)
            self.top.min=min(m1,m2)
            
        else:
            data.l=SegmentNode(data.range[0:len(data.range)//2])
            data.r=SegmentNode(data.range[len(data.range)//2:len(data.range)])
            m1,n1=self.build(data.l,False)
            m2,n2=self.build(data.r,False)
            data.max=max(m1,m2)
            data.min=min(n1,n2)
            return data.max,data.min
    def printAll(self,nd,first=True):
        if nd.l==None or nd.r==None:return
        if first:
            print(nd.range,nd.max,nd.min)
        else:
            print(nd.range,nd.max,nd.min)
        self.printAll(nd.l,False)
        self.printAll(nd.r,False)







class Node:
    def __init__(self, value):
        self.next = None
        self.data = value
class LinkedList:

    def __init__(self):

        self.node = None
        self.next = None
        self.__size=0

    def build(self,data):
        self.node=Node(data[0])
        temp=self.node
        self.__size += 1
        if len(data)!=1:
            for x in data[1:]:
                temp.next=Node(x)
                temp=temp.next
                self.__size+=1
    def printAll(self):
        temp=self.node
        for _ in range(self.__size):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def insert(self,data,place):
        last=self.node
        temp = last.next
        BackData=None
        if place!=1:
            for x in range(place-2):
                last=last.next
                temp=temp.next
            last.next=Node(data)
            last.next.next=temp
        else:
            self.node=Node(data)
            self.node.next=last
        self.__size+=1

class TreeNode:
    def __init__(self, data, father):
        self.value = data
        self.father = father
        self.hasChild = False
        self.child = []
class Tree:

    def __init__(self,root):

        self.__root=TreeNode(root,None)

    def add(self,data,father):#8 3
        print("-----------------------------")
        Root=self.__root
        if Root.value==father:
            Root.child.append(TreeNode(data,father))
            Root.hasChild=True
        else:
            dataFather=self.DFS(self.__root,father)
            dataFather.child.append(TreeNode(data,father))
            dataFather.hasChild=True
    def DFS(self,Node,targ):
        for child in Node.child:
            print(Node.father,child.value,targ)
            if child.value==targ:
                return child
            elif len(Node.child)==0:
                return None
            else:
                ans = self.DFS(child,targ)
                if ans!=None:
                    return ans
    def printAll(self):
        print(f"節點{self.__root.value}為根,其子節點為",end="")
        for child in self.__root.child:
            print(child.value,end=" ")
        print()
        print()
        for child in self.__root.child:
            self.__print(child)

    def __print(self,node):
        if node.hasChild:
            print(f"節點{node.value}的父節點為{node.father},子節點為",end="")
            for child in node.child:
                print(child.value,end=" ")
            print()
            print()
            for child in node.child:
                self.__print(child)
        else:
            print(f"節點{node.value}的父節點為{node.father},沒有子節點",end="")
            print()
            print()

'''if __name__=='__main__':

    LinkedListTest=False
    TreeTest=False
#------------------------------ LinkedList
    if LinkedListTest:
        list1=[1,2,3,4,5,6,7,8,9]
        LinkedList1=LinkedList()
        LinkedList1.build(list1)
        LinkedList1.printAll()
        LinkedList1.insert(20,3)
        LinkedList1.insert(20,5)
        LinkedList1.insert(20,7)
        LinkedList1.printAll()
    if TreeTest:
        Tree1=Tree(5)
        add=Tree1.add
        p=Tree1.printAll
        add(2,5)
        add(3,5)
        add(9,2)
        add(1,5)
        add(10,2)
        add(8,3)
        add(20,8)
        add(123123,20)
        add(34590,123123)
        p()

#------------------------------'''
def Help():
    print()
    print("LinkedList使用介紹")
    print("build方法可將list轉換為LinkedList")
    print("printAll可以將LinkedList內的元素列印出來")
    print("insert可以在對應的位置插入資料 如 insert(element,3)將會將element插入至第三個位置")

    print()
    print("Tree使用介紹")
    print("一開始建立物件需輸入Root的值")
    print("add可以將資料新增至對應的父節點下,如add(2,5)就是讓2成為節點5的Child")
    print("printAll可以印出所以節點(深度優先)")

