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

initial=(['b','c','d','a'],[])
final=(['a','b','c','d'],[])
Open=[(initial,None)]
Closed=[]
iter=0
while Open:
    curr=Open.pop()
    Closed.append(curr)
    old=copy.deepcopy(curr[0])
    if curr[0]==final:
        print("solution found!!")
        break
    if remove(curr[0]):
        flag=0
        for i in Closed:
            if i[0]==remove(curr[0]):
                flag=1
                break
        if not flag:
            Open.append((remove(curr[0]),old))
    for i in alpha:
        if stack(curr[0],i):
            flag=0
            for prev in Closed:
                if prev[0]==stack(curr[0],i):
                    flag=1
                    break
            if not flag:
                Open.append((stack(curr[0],i),old))
    iter+=1
    print(iter)
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
    for state in curr:
        print(state)
    print("--------------------------")