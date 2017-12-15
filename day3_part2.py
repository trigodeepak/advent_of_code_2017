#darw spiral
d = {}
def incr(i,j):
    inc = 0 
    if str(i+1)+str(j+1) in d:
        inc += d[str(i+1)+str(j+1)]
    if str(i+1)+str(j) in d:
        inc += d[str(i+1)+str(j)]
    if str(i+1)+str(j-1) in d:
        inc += d[str(i+1)+str(j-1)]
    if str(i-1)+str(j+1) in d:
        inc += d[str(i-1)+str(j+1)]
    if str(i-1)+str(j) in d:
        inc += d[str(i-1)+str(j)]
    if str(i-1)+str(j-1) in d:
        inc += d[str(i-1)+str(j-1)]
    if str(i)+str(j+1) in d:
        inc += d[str(i)+str(j+1)]
    if str(i)+str(j) in d:
        inc += d[str(i)+str(j)]
    if str(i)+str(j-1) in d:
        inc += d[str(i)+str(j-1)]
    return inc
def draw_spiral(last):
    n = 1
    xmax = 1
    ymax = 1
    xmin = 0
    ymin = 0 
    i = xmin
    j = ymin
    d['00']= 1
    while(n<last):
        while(i<xmax):
            d[str(i)+str(j)] = incr(i,j)
            if d[str(i)+str(j)]>last:
                return d[str(i)+str(j)]
            i+=1                        
        while(j<ymax):
            d[str(i)+str(j)] = incr(i,j)
            if d[str(i)+str(j)]>last:
                return d[str(i)+str(j)]
            j+=1
            
        xmin-=1
        ymin-=1
        while(i>xmin):
            d[str(i)+str(j)] = incr(i,j)
            if d[str(i)+str(j)]>last:
                return d[str(i)+str(j)]
            i-=1
            
        while(j>ymin):
            d[str(i)+str(j)] = incr(i,j)
            if d[str(i)+str(j)]>last:
                return d[str(i)+str(j)]
            j-=1
            
        xmax+=1
        ymax+=1
    
print draw_spiral(289326)
