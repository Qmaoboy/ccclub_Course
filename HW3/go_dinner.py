from itertools import combinations
def Godinner(_in):
    if not Check_total(_in):
        return False
    square_length=sum(map(int,_in.split(",")))//4
    _in=list(map(int,_in.split(",")))
    if max(_in)>square_length:
        return False
    subsetsum=powerset(_in,square_length)
    for i in subsetsum:
        if not _in:
            break
        for j in i:
            try:
                _in.remove(j)
            except:
                break
    if _in:
        return False
    else:
        return True

def powerset(_in,square_length):
    subset=[]
    for i in range(1,len(_in)+1):
        subset+=[j for j in combinations(_in,i) if sum(j)==square_length]
    return subset

def Check_total(_in):
    if sum(map(int,_in.split(",")))%4==0:
        return True
    return False
print(Godinner(input()))