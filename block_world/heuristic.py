alpha=['a','b','c','d']
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
            
                
    
    
    
    
    
    
    
final=(['a','b','c','d'],[])
print(heur((['b','c','d','a'],[])))