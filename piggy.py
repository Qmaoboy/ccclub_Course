class lucyispiggy():
    def __init__(self):
        self.x,self.y,self.r,self.d=list(map(int,input().split()))
        self.temp_judge=1
        self.femalepig=0
        self.getinput()
        self.getfemalepigindex()
        self.Calculate_density()
        self.Printresult()
        
    
    def getinput(self):
        self.maxtix=[]
        for _ in range(self.y+1):
            self.maxtix.append(list(map(int,input().split())))
            
    def getfemalepigindex(self):
        self.piggy=[]
        self.smallpiggy=0
        for i,ii in enumerate(self.maxtix):
            for j,jj in enumerate(ii):
                if jj==self.femalepig:
                    self.piggy.append((i,j))
                else:
                    self.smallpiggy+=jj
        self.temp_control=[0]*len(self.piggy)
        
    def Calculate_density(self):
        for idx,(i,j) in enumerate(self.piggy):
            Sumup=0
            for k in range(self.y+1):
                for g in range(self.x+1):
                    if (k-i)**2+(g-j)**2 <=self.r**2:
                        Sumup+=self.maxtix[k][g]
            Sumup-=self.maxtix[i][j]
            if float(Sumup/self.smallpiggy)*100>self.d:
                self.temp_control[idx]=1
        if any(self.temp_control):
            self.temp_judge=0
            
    def Printresult(self):
        
        print(f"{len(self.piggy)},{self.smallpiggy}")
        print(self.temp_judge,end="")


def sharonispiggy():
    x,y,r,d=list(map(int,input().split()))
    temp_judge,femalepig,smallpiggy=1,0,0
    matric,piggy=[],[]
    for _ in range(y+1):
        matric.append(list(map(int,input().split())))
    for i,ii in enumerate(matric):
            for j,jj in enumerate(ii):
                if jj==femalepig:
                    piggy.append((i,j))
                else:
                    smallpiggy+=jj
    temp_control=[0]*len(piggy)
    for idx,(i,j) in enumerate(piggy):
            Sumup=0
            for k in range(y+1):
                for g in range(x+1):
                    if (k-i)**2+(g-j)**2 <=r**2:
                        Sumup+=matric[k][g]
            Sumup-=matric[i][j]
            if float(Sumup/smallpiggy)*100>d:
                temp_control[idx]=1
    if any(temp_control):
        temp_judge=0
    print(f"{len(piggy)},{smallpiggy}")
    print(temp_judge,end="")
        
        
        
        
if __name__=="__main__":
    main=sharonispiggy()