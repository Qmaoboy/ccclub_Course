import re

class nlp2():
    def __init__(self) -> None:
        self.getinput()
        self.nlp_process()
        self.printresult()

    def getinput(self):
        self.text=[]
        self.keyword=sorted(input().split(),key=lambda x :len(x),reverse=True)
        while True:
            _intemp=input()
            if _intemp=="end":
                break
            else:
                self.text.append(_intemp)
    def printresult(self):
        for idx,i in enumerate(self.text):
            if idx==len(self.text)-1:
                print(i,end="")
            else:
                print(f"{i}")
            
    def nlp_process(self):

        for i, t in enumerate(self.text):
            for n, kw in enumerate(self.keyword):
                
                self.text[i] = re.sub(kw, f'<{n}>', self.text[i])
                # print(self.text[i])
                
            for n, kw in enumerate(self.keyword):
                self.text[i]=re.sub(f'<{n}>', f'「{kw}」',self.text[i])


def nlp_progress():
    text=[]
    keyword=sorted(input().split(),key=lambda x :len(x),reverse=True)
    while True:
        _intemp=input()
        if _intemp=="end":
            break
        else:
            text.append(_intemp)
    for i, t in enumerate(text):
        for n, kw in enumerate(keyword):
            text[i] = re.sub(kw, f'<{n}>', text[i])
                # print(self.text[i])
        for n, kw in enumerate(keyword):
            text[i]=re.sub(f'<{n}>', f'「{kw}」',text[i])
    for idx,i in enumerate(text):
        if idx==len(text)-1:
            print(i,end="")
        else:
            print(f"{i}")

if __name__=="__main__":
    main=nlp_progress()