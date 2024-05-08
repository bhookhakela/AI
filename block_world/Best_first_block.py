from collections import deque
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
    temp=[]
    curr=Open.pop()
    Closed.append(curr)
    if curr[0]==final: 
        print("solution found!!")
        break
    old=copy.deepcopy(curr[0])
    if remove(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==remove(curr[0]):
                flag=1
                break
        if not flag:
            temp.append((remove(curr[0]),old,heur(remove(curr[0]))))
    for i in alpha:
        if stack(curr[0],i):
            flag=0
            for prev in Closed:
                if prev[0]==stack(curr[0],i):
                    flag=1
                    break
            if not flag:
                temp.append((stack(curr[0],i),old,heur(stack(curr[0],i))))
    minimum=((None,None,-9999999999))
    for i in temp:
        if i[2]>minimum[2]:
            minimum=i
    Open.append(minimum)
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

    