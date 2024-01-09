s1=input()
s2=input()
target=len(s1) if len(s1)>len(s2) else len(s2)
res=""
for idx in range(target):
    if idx<len(s1):
        res+=s1[idx]
    if idx < len(s2):
        res+=s2[idx]
print(res)