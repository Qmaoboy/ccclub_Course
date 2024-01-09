def swap(ss,i,j):
    ss=list(ss)
    ss[i],ss[j]=ss[j],ss[i]
    return "".join(ss)
def judge(num):
    for i in range(len(num)):
        if num[i]!="9":
            max,maxi=int(num[i]),i
            for j in range(len(num)-1,i,-1):
                if int(num[j])>max:
                    max,maxi=int(num[j]),j
            if int(swap(num,i,maxi))>int(num):
                return swap(num,i,maxi)
    return num
print(judge(input()))