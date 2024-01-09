import re
class savemoney():
    def __init__(self):
        self.s = {"name":"S商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
        self.c = {"name":"C商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
        self.p = {"name":"P商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
        self.M = {"name":"M商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
        self.store_amount=[self.s,self.c,self.p,self.M]
        self.get_input()
        self.Print_the_min()
    def get_input(self):
        for store in self.store_amount:
            summery=input().split()
            store["amount"]=int(summery[0])
            for ss in range(1,len(summery)):
                if "免運" in summery[ss] or "運費" in summery[ss] :
                    store["shipping"]=self.getshiiping(summery[ss])
                elif summery[ss].isdigit():
                    store["price"]=float(summery[ss])
                elif "滿" in summery[ss]:
                    s= [list(map(float,s.split("打"))) for s in re.findall(r'\d*打\d*',summery[ss])]
                    s=[(ss[0],self.discountchange(ss[1])) for ss in s]
                    store["discount"]=s
                elif "%" in summery[ss]:
                    store["credit"]=float(summery[ss].replace("%",""))/100
            if store["amount"] > 0:
                self.get_discount_prices(store)
        
    def discountchange(self,number):
        if number >10:
            return number/100
        else:
            return number/10
    
    def getshiiping(self,text):
        shipping=text.replace("運費","")
        if shipping=="免運":
            return 0
        else:
            return int(shipping)

    def get_discount_prices(self,store):
        discountmax=1.0
        for eventdis in store["discount"]:
            if store["price"] > eventdis[0] and discountmax >eventdis[1]:
                discountmax=eventdis[1]

        store["Event_discount"]=discountmax
        store["Discount_prices"]=round(float((store["price"]*discountmax+store["shipping"])*(1-store["credit"])),0)
        
    def Print_the_min(self):
        min_store=self.s["name"]
        min_price=self.s["Discount_prices"]
        for i in self.store_amount:
            if i["Discount_prices"] < min_price and i["amount"]>0:
                min_store=i["name"]
                min_price=i["Discount_prices"]
        # print(self.store_amount)
        print(f"{min_store} {int(min_price)}")

def saving():
    s_t = {"name":"S商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
    c_t = {"name":"C商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
    p_t = {"name":"P商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
    M_t = {"name":"M商店","amount":0,"price":0,"shipping":0,"credit":0,"discount":[],"Discount_prices":0.0}
    store_amount=[s_t,c_t,p_t,M_t]
    for store in store_amount:
        summery=input().split()
        store["amount"]=int(summery[0])
        for ss in range(1,len(summery)):
            if "免運" in summery[ss] or "運費" in summery[ss] :
                shipping=summery[ss].replace("運費","")
                store["shipping"]=0 if shipping=="免運" else int(shipping)
            elif summery[ss].isdigit():
                store["price"]=float(summery[ss])
            elif "滿" in summery[ss]:
                s= [list(map(float,s.split("打"))) for s in re.findall(r'\d*打\d*',summery[ss])]
                s=[(ss[0],discountchange(ss[1])) for ss in s]
                store["discount"]=s
            elif "%" in summery[ss]:
                store["credit"]=float(summery[ss].replace("%",""))/100
        if store["amount"] > 0:
            discountmax=1.0
            for eventdis in store["discount"]:
                if store["price"] > eventdis[0] and discountmax >eventdis[1]:
                    discountmax=eventdis[1]

            store["Event_discount"]=discountmax
            store["Discount_prices"]=round(float((store["price"]*discountmax+store["shipping"])*(1-store["credit"])),0)
    min_store=s_t["name"]
    min_price=s_t["Discount_prices"]
    for i in store_amount:
        if i["Discount_prices"] < min_price and i["amount"]>0:
            min_store=i["name"]
            min_price=i["Discount_prices"]
    print(f"{min_store} {int(min_price)}")
def discountchange(number):
        if number >10:
            return number/100
        else:
            return number/10

if __name__=="__main__":
    main=saving()