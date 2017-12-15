with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    a = []
    for s in lines:
        a.append(int(s.strip()))
    i = 0
    while(i>=0 and i<= len(a)-1):
        a[i]+=1
        i += a[i]-1
        res+=1
    print res
