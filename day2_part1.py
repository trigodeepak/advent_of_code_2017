with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for s in lines:
        s = map(int,s.strip().split('\t'))
        res += max(s)-min(s)
    print res
