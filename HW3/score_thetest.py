def _getstu_(strnum):
    stu_list={}
    for i in range(int(strnum)):
        k=input().split()
        stu_list[i]={"name":k[0],"ans":"".join([j for j in k[1:]])}
    return stu_list
def Score(ground_truth,answer):
    result=[1 if ground_truth[i]==answer[i] else 0 for i in range(len(ground_truth))]
    score=sum([100/int(len(ground_truth)) if ground_truth[i]==answer[i] else 0 for i in range(len(ground_truth))])
    return score,result
  
def main_(ans=input(),stu_num=input()):
    from operator import add
    ans="".join(ans.split())
    Correct_rate=[0]*len("".join(ans))
    stu_list=_getstu_(stu_num)

    for nn in range(int(stu_num)):
        score,result=Score(ans,stu_list[nn]["ans"])
        stu_list[nn].update({
            "score":score,
            "result":result
        })
        Correct_rate=list( map(add, Correct_rate, result) )
    Correct_rate=[f"{round(i/int(stu_num)*100,2)}%" for i in Correct_rate]
    for key,value in stu_list.items():
        print(f"{value['name']} {int(value['score'])}")
    print(" ".join(Correct_rate))
main_()