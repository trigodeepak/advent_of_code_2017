import operator
with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    d = {}
    for s in lines:
        s = s.strip().split()
        if s[0] not in d:
            d[s[0]] = 0
        if s[4] not in d:
            d[s[4]] = 0
        if s[5] == '>':
            if d[s[4]] > int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
        elif s[5] == '<':
            if d[s[4]] < int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
        elif s[5] == '<=':
            if d[s[4]] <= int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
        elif s[5] == '>=':
            if d[s[4]] >= int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
        elif s[5] == '==':
            if d[s[4]] == int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
        elif s[5] == '!=':
            if d[s[4]] != int(s[6]):
                if s[1] == 'inc':
                    d[s[0]] = d[s[0]] + int(s[2])
                else:
                    d[s[0]] = d[s[0]] - int(s[2])
    b = max(d.iteritems(), key=operator.itemgetter(1))[0]
    print d[b]
