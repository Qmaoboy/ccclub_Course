def Game_search(start,Prefix,next_,value,_in,count,gothrough):
    now=next_
    gothrough.append(now)
    count+=1
    if count ==len(_in):
        if start in value and len(gothrough)==len(_in)-1:
            return True
        else:
            return False

    if value[0] in gothrough and value[1] in gothrough:
        return False 
    next_= value[0] if value[0] not in gothrough and value[0] != start else value[1]
    return Game_search(start,now,next_,_in[next_],_in,count,gothrough)

_in={}
while True:
    try:
        answer=input().split()
        if not answer:
            break
        else:
            _in[answer[0]]=[answer[1],answer[2]]
    except:
        break

from random import randint
Persons=list(_in.keys())
start_,next_=Persons[0],_in[Persons[0]][randint(0,1)],
countidx=1
gothrough=list()
print(Game_search(start_,start_,next_,_in[next_],_in,countidx,gothrough))