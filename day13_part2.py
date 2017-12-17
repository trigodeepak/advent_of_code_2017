with open('input.txt') as f:
    lines = f.readlines()
    d = [[] for i in xrange(2)]
    for s in lines:
        s = s.strip().split(' ')
        d[0].append(int(s[0][:-1]))
        d[1].append(int(s[1]))
    
    for j in xrange(1,3966417):
        res = 0 
        for i in range(len(d[0])):
            ind = d[0][i]+j-1
            cond = d[1][i]+d[1][i]-2
##            print ind, cond
            if ind % cond == 0:
                res = 1
##                print "chage in res"
                break
        if res == 0:
            print j-1
            break
        
