with open('input.txt') as f:
    lines = f.read()
    s = 0
    n = len(lines)
    mid = n/2
    for i in xrange(n-mid):
        if lines[i] == lines[i+mid]:
            s+=int(lines[i])
    j=0
    for i in xrange(n-mid,n):
        if lines[j] == lines[i]:
            s+=int(lines[i])
        j+=1
    print s
