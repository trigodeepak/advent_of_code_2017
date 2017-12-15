with open('input.txt') as f:
    lines = f.readlines()
    res = 0 
    for s in lines:
        s = s.strip().split(' ')
        s.sort()
        f = 0
        for i in xrange(len(s)-1):
            if s[i] == s[i+1]:
                f = 1
                break
        if f == 0:
            res+=1
    print res
