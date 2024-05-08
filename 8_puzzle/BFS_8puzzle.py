from collections import deque
import copy
initial=[[2,0,3],[1,8,4],[7,6,5]]
final=[[1,2,3],[8,0,4],[7,6,5]]
def find(mat):
    for rowind in range(len(mat)):
        for colind in range(len(mat[0])):
            if mat[rowind][colind]==0:
                return [rowind,colind]
def moveleft(mat):
    blank=find(mat)
    if blank[1]-1>=0:
        new=copy.deepcopy(mat)
        left_tile=[blank[0],blank[1]-1]
        temp=new[left_tile[0]][left_tile[1]]
        new[left_tile[0]][left_tile[1]]=new[blank[0]][blank[1]]
        new[blank[0]][blank[1]]=temp
        return new
    return None
def moveright(mat):
    blank=find(mat)
    if blank[1]+1<3:
        new=copy.deepcopy(mat)
        right_tile=[blank[0],blank[1]+1]
        temp=new[right_tile[0]][right_tile[1]]
        new[right_tile[0]][right_tile[1]]=new[blank[0]][blank[1]]
        new[blank[0]][blank[1]]=temp
        return new
    return None
def movetop(mat):
    blank=find(mat)
    if blank[0]-1>=0:
        new=copy.deepcopy(mat)
        top_tile=[blank[0]-1,blank[1]]
        temp=new[top_tile[0]][top_tile[1]]
        new[top_tile[0]][top_tile[1]]=new[blank[0]][blank[1]]
        new[blank[0]][blank[1]]=temp
        return new
    return None
def movebelow(mat):
    blank=find(mat)
    if blank[0]+1<3:
        new=copy.deepcopy(mat)
        below_tile=[blank[0]+1,blank[1]]
        temp=new[below_tile[0]][below_tile[1]]
        new[below_tile[0]][below_tile[1]]=new[blank[0]][blank[1]]
        new[blank[0]][blank[1]]=temp
        return new
    return None

Open=deque([(initial,None)])
Closed=[]  
iter=0
while Open:
    curr=Open.popleft()
    Closed.append(curr)
    if curr[0]==final: 
        break
    old=copy.deepcopy(curr[0])
    if moveleft(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==moveleft(curr[0]):
                flag=1
                break
        if not flag:
            Open.append((moveleft(curr[0]),old))
    if moveright(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==moveright(curr[0]):
                flag=1
                break
        if not flag:
            Open.append((moveright(curr[0]),old))
    if movetop(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==movetop(curr[0]):
                flag=1
                break
        if not flag:
            Open.append((movetop(curr[0]),old))
    if movebelow(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==movebelow(curr[0]):
                flag=1
                break
        if not flag:
            Open.append((movebelow(curr[0]),old))
    iter+=1
    print(iter)
    # print(Open,"\n")
print('done')
solution=[]
i=len(Closed)-1

while i>0 :
    solution.append(Closed[i][0])
    for j in range(len(Closed)):
        # print(j)
        if Closed[i][1]==Closed[j][0]:
            i=j
            break
    # print(i)
solution.append(Closed[i][0])
for curr in solution[::-1]:
    for mat in curr:
        print(mat)
    print("--------------------------")
    