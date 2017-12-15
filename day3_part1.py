#darw spiral
def draw_spiral(last):
    n = 1
    xmax = 1
    ymax = 1
    xmin = 0
    ymin = 0 
    i = xmin
    j = ymin
    while(n<last):
        while(i<xmax):
            n+=1
            i+=1
            if(n==last):
                print abs(i)+abs(j)
                return
        while(j<ymax):
            n+=1
            j+=1
            if(n==last):
                print abs(i)+abs(j)
                return
        xmin-=1
        ymin-=1
        while(i>xmin):
            n+=1
            i-=1
            if(n==last):
                print abs(i)+abs(j)
                return
        while(j>ymin):
            n+=1
            j-=1
            if(n==last):
                print abs(i)+abs(j)
                return 
        xmax+=1
        ymax+=1
    
draw_spiral(289326)
