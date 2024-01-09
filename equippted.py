class getequipted():
    def __init__(self):
        self.item_menu=dict()
        # self.amount=[self.Get_rule_1(),self.Get_rule_2()]
        self.requirelist=[]
        self.Get_itemlist()
        self.Get_requirelist()

    def Get_itemlist(self):
        item_number=int(input())
        for _ in range(item_number):
            requireitem=[]
            menu={}
            item_mapping=list(input().split())
            item,money=item_mapping[0],int(item_mapping[1])
            if len(item_mapping)>2:
                requireitem=item_mapping[2:]
            menu["money"]=money
            menu["require"]=requireitem
            menu["addmoney"]=0
            self.item_menu[item]=menu
        else:
            
            for i in list(self.item_menu.keys()):
                if self.item_menu[i]["require"]:
                    self.UpdatePrice(i)
        
            for i in list(self.item_menu.keys()):
                self.item_menu[i]["money"]+=self.item_menu[i]["addmoney"] 

    def UpdatePrice(self,target):
    
        if self.item_menu[target]["require"]:
            self.item_menu[target]["addmoney"]=sum([self.UpdatePrice(i) for i in self.item_menu[target]["require"]])
            return self.item_menu[target]["money"]+self.item_menu[target]["addmoney"]
        else:
            return self.item_menu[target]["money"]
        
    def Get_requirelist(self):
        require_item=int(input())
        for _ in range(require_item):
            self.requirelist.append(input())

    def Get_require_money(self):
        for i in self.requirelist:
            print(self.item_menu[i]["money"])

gg=getequipted()
gg.Get_require_money()