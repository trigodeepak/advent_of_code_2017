with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for s in lines:
        s = map(int,s.strip().split('\t'))
        s.sort()
        n = len(s)
        count = 1
        for i in xrange(n):
            for j in xrange(n-1,i,-1):
                if s[j]%s[i] == 0:
                    count = max(count,s[j]/s[i])
        res += count
    print res
