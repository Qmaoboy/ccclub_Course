# ccclub_Course Lecture 
## 測試使用方式
```python=
import os,sys,glob
class Unitest():
    def __init__(self,Test_name,projectname):
        self.testname=Test_name
        self.projectname=projectname
        self.test_porogram()
        
    def test_porogram(self):
        if os.path.isfile(self.projectname):
            # self.inputfile=glob.glob(f"./{self.testname}/*.in")
            # self.outputfile=glob.glob(f"./{self.testname}/*.out")
            for idx in range(1,11):
                os.system(f"python {self.projectname} < ./{self.testname}/{idx}.in > ./{self.testname}/{idx}_result.out")
                kk=os.system(f"diff ./{self.testname}/{idx}.out ./{self.testname}/{idx}_result.out > ./{self.testname}/{idx}_Compare.txt")
                if kk==0:
                    print(f"Test {idx} Pass")
                else:
                    print(f"Test {idx} Fail")
if __name__=="__main__":
    Test_name=["文句處理","省錢小作戰","推薦系統","小仔養豬","S型分班"]
    Projectname=["nlp.py","Save_money.py","recommandsystem.py","piggy.py","Sclass.py"]
    for test,project in zip(Test_name,Projectname):
        print(test,project)
        main=Unitest(test,project)
```
在Test_name 以及 Projectname 分別輸入對應的檔案路徑名稱 直接執行即可。

## HW1
1. 凱凱的出門準備 ()
2. 字串加密 ()
3. 小明寫論文()
4. 字首學習法 ()
5. 串列切割 ()

## HW2
1. 字串合併()
2. 小仔遊七福村 ()
3. 凱凱堆積木()
4. 小仔可不可 ()
5. 加簽大地 II ()

## HW3
1. 數字交換最大值
2. 改考卷
3. 小明上菜拉IV
4. 出裝備
5. 手拉手團康遊戲

## HW4
1. 文句處理
2. 省錢小作戰
3. 推薦系統
4. 小仔養豬
5. S 型分班