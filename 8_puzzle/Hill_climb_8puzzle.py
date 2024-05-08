from collections import deque
import random
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
def heur(mat):
    val=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=final[i][j]:
                val+=1
    return val
    

Open=[(initial,None,heur(initial))]
Closed=[]  
temp=[]
iter=0
while Open:
    curr=Open.pop()
    Closed.append(curr)
    if curr[0]==final: 
        break
    old=copy.deepcopy(curr[0])
    flag=0
    mainflag=0
    for i in range(4):
        curr_cpy=copy.deepcopy(curr)
        # curr_cpy2=copy.deepcopy(curr)n
        randidx=random.randint(1,4)
        
        if randidx==1:
            if moveleft(curr_cpy[0]):
                mainflag=1
                temp=moveleft(curr_cpy[0])
            
        elif randidx==2:
            if moveright(curr_cpy[0]):
                mainflag=1
                temp=moveright(curr_cpy[0])
        elif randidx==3:
            if movetop(curr_cpy[0]):
                mainflag=1
                temp=movetop(curr_cpy[0])
        elif randidx==4:
            if movebelow(curr_cpy[0]):
                mainflag=1
                temp=movebelow(curr_cpy[0])
        
        # curr_cpy2=copy.deepcopy(curr)
        # temp=temp_func(curr_cpy2[0])
        if heur(temp)<heur(old):
            flag=1
            Open.append((temp,old,heur(temp)))
            break
    if not flag:
        print("solution not found")
        break
    if mainflag==0:
        print("no possible allocation")
        break
    
    iter+=1
    print(iter)
    # print(Open,"\n")

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

    