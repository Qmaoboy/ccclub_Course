from random import randint
class Ggraph():
    def __init__(self):
        self._path_=dict()
        self.count=1
        self.trajectory=list()
        self.result=False
        self.get_input()

    def get_input(self):
        while True:
            try:
                ans=input().split()
                if not ans:
                    break
                else:
                    self._path_[ans[0]]=[ans[1],ans[2]]
            except:
                break
        self.pathlength=len(self._path_)   
        self.init_start()     
    def init_start(self):
        shuffle_start=randint(0,self.pathlength-1)
        self.start = list(self._path_.keys())[shuffle_start]
        self.next= self._path_[self.start][randint(0,1)]
        self.DFS()
    def DFS(self):
        now=self.next
        value=self._path_[now]
        self.trajectory.append(now)
        self.count+=1
        if self.count ==self.pathlength:
            if self.start in value and len(self.trajectory)==self.pathlength-1:
                self.result=True
                return True
            else:
                self.result=False
                return False
            
        if value[0] in self.trajectory and value[1] in self.trajectory:
            self.result=False
            return False 
        
        self.next= value[0] if value[0] not in self.trajectory and value[0] != self.start else value[1]
        # print(self.trajectory,self.next,self._path_[self.next],self.start,len(self.trajectory),self.pathlength-1)
        return self.DFS()

print(Ggraph().result)

                     


