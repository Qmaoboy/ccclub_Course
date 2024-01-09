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