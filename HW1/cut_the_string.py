def p5(cin):
    if not cin:
        return False
    try:
        cin=list(map(float,cin.split(",")))
    except:
        return False
    idx=0
    for i in range(len(cin)):
        if sum(cin[:idx])==sum(cin[idx:]):
            return True
        else:
            idx+=1
    return False

print(p5(input()))