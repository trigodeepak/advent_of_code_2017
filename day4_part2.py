with open('input.txt') as f:
    lines = f.readlines()
    res = 0 
    for a in lines:
        a = a.strip().split()
        c = []
        for i in a:
            b = list(i)
            b.sort()
            c.append(''.join(b))
        c.sort()
        s = c
        f = 0
        for i in xrange(len(s)-1):
            if s[i] == s[i+1]:
                f = 1
                break
        if f == 0:
            res+=1
    print res
