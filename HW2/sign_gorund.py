def cond1(k):
    return [i for i in k if i[3:6]=="902"],[i for i in k if i[3:6]=="901"],[i for i in k if i[3:6]!="902" and i[3:6]!="901"]
def cond2(k):
    return [i for i in k if i[:3]=="a04" and times(i)]+[i for i in k if i[:3]=="a04" and not times(i)]+[i for i in k if i[:3]!="a04" and times(i)]+[i for i in k if i[:3]!="a04" and not times(i)]
def times(k):
    return True if int(k[-3:])%3==0 or int(k[-3:])%5==0 or int(k[-3:])%7==0 else False
d1=cond1(input().split())
d2=list(map(cond2,d1))
for d in [k for i in d2 for k in i]:
    print(d)