def MergeSort(List):
    if len(List)==1:
        return List
    Left=MergeSort(List[0:len(List)//2])
    Right=MergeSort(List[len(List)//2:len(List)])
    Left.reverse()
    Right.reverse()
    nowList=[]
    while True:
        if len(Left)==0 or len(Right)==0:
            break
        if Left[-1]>Right[-1]:
            nowList.append(Right[-1])
            Right.pop()
        else:
            nowList.append(Left[-1])
            Left.pop()
    if len(Left)==0:
        while len(Right)!=0:
            nowList.append(Right[-1])
            Right.pop()
    else:
        while len(Left) != 0:
            nowList.append(Left[-1])
            Left.pop()
    return nowList