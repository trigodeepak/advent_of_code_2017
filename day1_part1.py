with open('input.txt') as f:
    lines = f.read()
    s = 0
    for i in xrange(len(lines)-1):
        if lines[i] == lines[i+1]:
            s+=int(lines[i])
    if lines[0] == lines[len(lines)-1]:
        s+=int(lines[0])
    print s
