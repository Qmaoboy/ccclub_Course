from itertools import combinations
class hsiao_ming():
    def __init__(self):
        self.wood=list(map(int,input().split(",")))
        self.square_length=sum(self.wood)//4
        self.subsetsum=self.powerset()

    def chekc_total(self):
        if not self.wood:
            return False
        if sum(self.wood) %4!=0:
            return False
        if max(self.wood) >self.square_length:
            return False
    
    def Check_wood(self):
        self.chekc_total()
        for i in self.subsetsum:
            if not self.wood:
                break
            for j in i:
                try:
                    self.wood.remove(j)
                except:
                    break

        if self.wood:
            return False
        else:
            return True

    def powerset(self):
        subset=[]
        for i in range(1,len(self.wood)+1):
            subset+=[j for j in combinations(self.wood,i) if sum(j)==self.square_length]
        return subset

gg=hsiao_ming()
print(gg.Check_wood())