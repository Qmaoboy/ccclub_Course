class sclass():
    def __init__(self) -> None:
        self.rank_dict={}
        self.getinput()
        self.get_sequence()
        
    def getinput(self):
        stu=input().split()
        rank=input().split()
        for r,s in zip(rank,stu):
            self.rank_dict.setdefault(r, []).append(s)
            
    def get_sequence(self):        
        seq=sorted(self.rank_dict.keys(),reverse=False)
        seq_print=[]
        while True:
            for key in seq:
                if self.rank_dict[key]:
                    seq_print.append(self.rank_dict[key].pop(0))
                          
            for key in seq[::-1]:
                if self.rank_dict[key]:
                    seq_print.append(self.rank_dict[key].pop(0))
                    
            if all([len(v)==0 for v in self.rank_dict.values()]):
                break
        print(" ".join(seq_print))

def S_type_divide():
    rank_dict={}
    stu=input().split()
    rank=input().split()
    for r,s in zip(rank,stu):
        rank_dict.setdefault(r, []).append(s)
    seq=sorted(rank_dict.keys(),reverse=False)
    seq_print=[]
    while True:
        for key in seq:
            if rank_dict[key]:
                seq_print.append(rank_dict[key].pop(0))
                        
        for key in seq[::-1]:
            if rank_dict[key]:
                seq_print.append(rank_dict[key].pop(0))
        if all([len(v)==0 for v in rank_dict.values()]):
            break
    print(" ".join(seq_print))
    

if __name__=="__main__":
    main=S_type_divide()