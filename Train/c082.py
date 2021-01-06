import sys
fall=[]
def turnRight(Data):
    data=Data
    if Data[2]=="N":
        data[2]="E"
    elif Data[2] == "E":
        data[2]="S"
    elif Data[2] == "W":
        data[2]="N"
    elif Data[2] == "S":
        data[2]="W"
    return data
def turnLeft(Data):
    data=Data
    if Data[2]=="N":
        data[2]="W"
    elif Data[2] == "E":
        data[2]="N"
    elif Data[2] == "W":
        data[2]="S"
    elif Data[2] == "S":
        data[2]="E"
    return data
def forward(Data):
    data=Data
    if Data[2]=="N":
        data[1]+=1
    elif Data[2] == "E":
        data[0]+=1
    elif Data[2] == "W":
        data[0]-=1
    elif Data[2] == "S":
        data[1]-=1

    return data
for inp in sys.stdin:
    x,y=map(int,inp.split())
    for data in sys.stdin:
        nowX, nowY, nowT = data.split()
        nowX,nowY=int(nowX),int(nowY)
        DATA=[nowX,nowY,nowT]
        command=input()
        last=DATA.copy()
        f=True

        for c in command:
            if c=="R":
                DATA=turnRight(DATA).copy()
            if c=="L":
                DATA=turnLeft(DATA).copy()
            if c=="F":
                DATA=forward(DATA).copy()
            if DATA[0]>x or DATA[0]<0:
                if last not in fall:
                    fall.append(last[0:1])
                    print(last[0], last[1], last[2],"LOST")
                    f=False
                    break
                else:
                    DATA=last.copy()



            elif DATA[1]>y or DATA[1]<0:
                if last[0:1] not in fall:
                    fall.append(last[0:1])
                    print(last[0], last[1], last[2], "LOST")
                    f = False
                    break
                else:
                    DATA=last.copy()
            last=DATA.copy()
        if f:
            print(DATA[0],DATA[1],DATA[2])