from collections import deque
import random
import copy
alpha=['a','b','c','d']
def remove(state):
    stk=copy.deepcopy(state[0])
    floor=copy.deepcopy(state[1])
    if stk:
        floor.append(stk.pop())
        return (stk,floor)
    else:
        return None

def stack(state,item):
    stk=copy.deepcopy(state[0])
    floor=copy.deepcopy(state[1])
    if floor:
        if item in floor:
            stk.append(item)
            floor.remove(item)
            return(stk,floor)
        else:
            # print('Not in floor')
            return None
    else:
        return None
def heur(state):
    val=0
    stk=state[0]
    flr=state[1]
    for ele in alpha:
        if ele in final[0]:
            final_ind=final[0].index(ele)
            if ele in stk:
                curr_ind=stk.index(ele)
                if final_ind-1>=0 and curr_ind-1>=0:
                    if final[0][final_ind-1]==stk[curr_ind-1]:
                        val+=1
                    else:
                        val-=1
                elif final_ind-1<0 and curr_ind-1<0:
                    val+=1
                else:
                    val-=1
            else:
                if final_ind-1<0:
                    val+=1
                else:
                    val-=1
        elif ele in final[1]:
            if ele in stk:
                curr_ind=stk.index(ele)
                if curr_ind-1<0:
                    val+=1
                else:
                    val-=1
            if ele in flr:
                val+=1
    return val

initial=(['b','c','d','a'],[])
final=(['a','b','c','d'],[])
Open=[(initial,None,heur(initial))]
Closed=[]
iter=0
while Open:
    curr=Open.pop()
    Closed.append(curr)
    if curr[0]==final: 
        break
    old=copy.deepcopy(curr[0])
    flag=0
    flag2=0
    mainflag=0
    start,end=1,5
    for i in range(5):
        flag2=0
        curr_cpy=copy.deepcopy(curr)
        # curr_cpy2=copy.deepcopy(curr)n

        randidx=random.randint(start,end)
        
        if randidx==1:
            if remove(curr_cpy[0]):
                flag2=1
                mainflag=1
                temp=remove(curr_cpy[0])
            
        elif randidx==2:     
            if stack(curr_cpy[0],'a'):
                flag2=1
                mainflag=1
                temp=stack(curr_cpy[0],'a')
        elif randidx==3:     
            if stack(curr_cpy[0],'b'):
                flag2=1
                mainflag=1
                temp=stack(curr_cpy[0],'b')
        elif randidx==4:     
            if stack(curr_cpy[0],'c'):
                flag2=1
                mainflag=1
                temp=stack(curr_cpy[0],'c')
        elif randidx==5:     
            if stack(curr_cpy[0],'d'):
                flag2=1
                mainflag=1
                temp=stack(curr_cpy[0],'d')
                    

        
        
        if flag2 and heur(temp)>heur(old):
            flag=1
            Open.append((temp,old,heur(temp)))
            break
        end-=1
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

    