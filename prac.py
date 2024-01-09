while True:
    try:
        ans=input().split()
        if not ans:
            break
        else:
            self._path_[ans[0]]=[ans[1],ans[2]]
    except:
        break
