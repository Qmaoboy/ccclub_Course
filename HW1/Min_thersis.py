a=input().split()
res=[]
for idx,word in enumerate(a):
    if word in ["to","the","is","for","of","and","in","a","an","from"] and idx!=0 and idx!=len(a)-1:
        res.append(word[0]+word[1:])
    else:
        res.append(word[0].upper()+word[1:])

print(" ".join(res))