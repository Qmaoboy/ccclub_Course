
def onedayjudge(drinksum):
    caffein,suger=drinksum
    if caffein >300:
        return False
    if suger >60:
        return False
    return True
def threedayjudge(drinksum):
    caffein,suger=drinksum
    if caffein >700:
        return False
    if suger >150:
        return False
    return True
def define_drink(dd:str,curremt_drink_sum:list)->list:
    from operator import add
    for idx,i in enumerate(dd):
        if i =="B":
            curremt_drink_sum=list(map(add,[int(dd[idx+1:])*50,int(dd[idx+1:])*10],curremt_drink_sum))
        elif i=="M":
            curremt_drink_sum=list(map(add,[int(dd[idx+1:])*20,int(dd[idx+1:])*30],curremt_drink_sum))
    return curremt_drink_sum
d1=input()
d2=input()
d3=input()
threedayDrink=[define_drink(i,[0,0]) for i in [d1,d2,d3]]
totaldrink=[sum([i[0] for i in threedayDrink]),sum([i[1] for i in threedayDrink])]
one_day_pass=list(map(onedayjudge,threedayDrink))
if all(one_day_pass) and threedayjudge(totaldrink):
    print("可")
else:
    print("不可")