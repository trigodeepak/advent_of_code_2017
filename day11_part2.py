import operator
with open('input.txt') as f:
    lines = f.readline()
    lines = (lines.strip().split(','))
    x=y=z=0
    m = 0
    for i in lines:
        if i == 'ne':
            y-=1
            x+=1
        elif i == 'se':
            y-=1
            z+=1
        elif i == 's':
            x-=1
            z+=1
        elif i == 'sw':
            y+=1
            x-=1
        elif i == 'nw':
            y+=1
            z-=1
        elif i == 'n':
            x+=1
            z-=1
        m = max(m,(abs(x)+abs(y)+abs(z))/2)
    print m
