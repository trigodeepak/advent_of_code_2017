with open('input.txt') as f:
    lines = f.readline()
    lines = lines.strip().split(',')
    i = ord('a')
    l = ord('p')
    s = []
    while(i<=l):
        s.append(chr(i))
        i+=1
    for a in lines:
        if a[0] == 'x':
            b = a.split('/')
            x = int(b[0][1:])
            y = int(b[1])
            t = s[x]
            s[x] = s[y] 
            s[y] = t
        elif a[0] == 'p':
            k = s.index(a[3])
            s[s.index(a[1])] = a[3]
            s[k] = a[1]
        elif a[0] == 's':
            x = int(a[1:])
            s = s[-x:]+s[:-x]
    print ''.join(s)
