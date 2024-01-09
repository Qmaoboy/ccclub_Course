def p4(a):
    a=a.split(",")
    res=""
    vomin=99999999999999999999999999999999999
    t=0
    for i in a:
        if len(i)<=vomin:
            vomin=len(i)
            t=i
    for idx in range(vomin):
        for i in a:
            if i[idx]!=t[idx]:
                return res
        res+=t[idx]
    return res
res=p4(input())
if res:
    print( res)
else:
    print("No common")