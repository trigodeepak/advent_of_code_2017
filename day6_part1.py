with open('input.txt') as f:
    lines = f.readlines()
    res = 0 
    for s in lines:
        s = map(int,s.strip().split('\t'))
    d = {}
    n = len(s)
    x = [str(x) for x in s]
    d[''.join(x)] = 1
    m = max(s)
    i = s.index(m)
    s[i] = 0
    k = i
    while(m>0):
        k+=1
        if(k>=n):
            k = 0
        s[k]+=1
        m-=1
    print s
    x = [str(x) for x in s]
    count = 1
    while(''.join(x) not in d):
        m = max(s)
        i = s.index(m)
        s[i] = 0
        k = i
        while(m>0):
            k+=1
            if(k>=n):
                k = 0
            s[k]+=1
            m-=1
##        print s
        d[''.join(x)] = 1
        x = [str(x) for x in s]
        count+=1
    print count 
