class recommand():
    def __init__(self):
        self.similarity=int(input())
        self.man={}
        self.getinput()
        self.main()
    def getinput(self):
        while True:
            input_=input()
            if input_=="end":
                break
            else:
                input_=input_.split()
                self.man[input_[0]]={}
                self.man[input_[0]]["Buy"]=list(input_[1:])
        
    def get_similarity(self,man1,man2):
        similarity=float(len([jj for jj in self.man[man1]["Buy"] if jj in self.man[man2]["Buy"]])/len(self.man[man1]["Buy"]))*100
        return similarity
    
    def Recommand_list(self,person):
        self.man[person]["Recommand"]=[]
        self.man[person]["Similarity"]={}
        for i in self.man.keys():
            if i!=person:
                self.man[person]["Similarity"][i]=self.get_similarity(person,i)
                if self.man[person]["Similarity"][i] >=self.similarity:
                    for kk in self.man[i]["Buy"]:
                        if kk not in self.man[person]["Buy"] and kk not in self.man[person]["Recommand"]:
                            self.man[person]["Recommand"].append(kk)
    def printkey(self,key,idx):
        if self.man[key]["Recommand"]:
            if idx==len(self.man.keys()):
                print(key," ".join(self.man[key]["Recommand"]),end="")
            else:
                print(key," ".join(self.man[key]["Recommand"]))
        else:
            if idx==len(self.man.keys()):
                print(key,end="")
            else:
                print(key)
    
    def main(self):
        for idx,key in enumerate(self.man.keys()):
            self.Recommand_list(key)
            self.printkey(key,idx)
        # print(self.man)
        
        
        
def recommsys():
    similarity=int(input())
    human={}
    while True:
        input_=input()
        if input_=="end":
            break
        else:
            input_=input_.split()
            human[input_[0]]={}
            human[input_[0]]["Buy"]=list(input_[1:])
    for idx,hkey in enumerate(human.keys()):
        human=Get_recom_list(human,similarity,hkey)
        if human[hkey]["Recommand"]:
            if idx==len(human.keys()):
                print(hkey," ".join(human[hkey]["Recommand"]),end="")
            else:
                print(hkey," ".join(human[hkey]["Recommand"]))
        else:
            if idx==len(human.keys()):
                print(hkey,end="")
            else:
                print(hkey)
        
def Get_recom_list(human,similarity,person):
    human[person]["Recommand"]=[]
    human[person]["Similarity"]={}
    for i in human.keys():
        if i!=person:
            human[person]["Similarity"][i]=float(len([jj for jj in human[person]["Buy"] if jj in human[i]["Buy"]])/len(human[person]["Buy"]))*100
            if human[person]["Similarity"][i] >=similarity:
                for kk in human[i]["Buy"]:
                    if kk not in human[person]["Buy"] and kk not in human[person]["Recommand"]:
                        human[person]["Recommand"].append(kk)           
    return human
    
if __name__=="__main__":
    main=recommsys()