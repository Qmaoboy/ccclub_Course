import math
a,b,c=input(),input(),input()
def event1(a,b,c):
    same_gender=0.8 if len(set([a[1],b[1],c[1]]))==1 else 1
    diff_born_place=0.8 if len(set([a[0],b[0],c[0]]))==3 else 1
    return math.ceil((basis_count(a)+basis_count(b)+basis_count(c))*same_gender*diff_born_place)
    
def event2(a,b,c):
    e2sum=0
    for i in [a,b,c]:
        e2sum+=basis_count(i)+count_7(i)+time_7(i)
    return e2sum
def count_7(k):
    sum_=0
    for i in k:
        if i=="7":
            sum_+=1
    return -70*sum_

def time_7(k):
    if int(k[-3:])%7==0:
        return -77
    else:
        return 0
def basis_count(a):
    return 599 if a[0]=="O" else 699

# print(event1(a,b,c))
# print(event2(a,b,c))

print(min(event1(a,b,c),event2(a,b,c)))