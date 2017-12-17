with open('input.txt') as f:
    lines = f.readlines()
    d = [[] for i in xrange(2)]
    for s in lines:
        s = s.strip().split(' ')
        d[0].append(int(s[0][:-1]))
        d[1].append(int(s[1]))
    res = 0
    for i in range(1,len(d[0])):
        ind = d[0][i]
        cond = d[1][i]+d[1][i]-2
        while ind >= cond:
            ind-= cond
        if ind == 0:
            res+= d[0][i]*d[1][i]   
    print res
