def get_itemlist(item_num):
    item_list={}
    for i in range(int(item_num)):
        item_=input().split()
        item_list[item_[0]]={"Price":int(item_[1]),"requireitem":[]}
        if len(item_)>2:
            item_list[item_[0]].update({"requireitem":item_[2:]})
    return item_list
def get_value(item,item_list):
    if item_list[item]["requireitem"]:
        return item_list[item]["Price"]+sum([get_value(i,item_list) for i in item_list[item]["requireitem"]])
    else:
        return item_list[item]["Price"]
def update_price(item_list):
    for key,value in item_list.items():
        value.update({"Update Price":get_value(key,item_list)})
    return item_list
    
def get_requrirelist(require_item,item_list):
    requre_list={}
    for i in range(int(require_item)):
        require_=input().split()
        print(item_list[require_[0]]["Update Price"])

item_list=get_itemlist(input())
get_requrirelist(input(),update_price(item_list))