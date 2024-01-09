class getargmax():
    def __init__(self,number):
        self.number=number
        self.long=len(self.number)
        self.result=self.compare()
    def swap(self,i,j):
        listnumber=list(self.number)
        listnumber[i],listnumber[j]=listnumber[j],listnumber[i]
        return "".join(listnumber)
    def compare(self):
        for i in range(self.long):
            if self.number[i]!="9":
                now_max,maxi=int(self.number[i]),i
                for j in range(self.long-1,i,-1):
                    if int(self.number[j])>now_max:
                        now_max,maxi=int(self.number[j]),j
                if int(self.swap(i,maxi))>int(self.number):
                    return self.swap(i,maxi)
        return self.number
gg=getargmax(input())
print(gg.result)
