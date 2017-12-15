with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    a = []
    for s in lines:
        a.append(int(s.strip()))
    i = 0
    while(i>=0 and i<= len(a)-1):
        x = a[i]
        if a[i]<3:
            a[i]+=1
        else:
            a[i]-=1
        i += x
        res+=1
    print res
