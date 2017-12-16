import operator
with open('input.txt') as f:
    lines = f.readline()
    lines = map(int,lines.strip().split(','))
    print lines
    size = 256
    a  = []
    for i in xrange(size+1):
    	a.append(i)
    sk = -1
    start = 0 
    end = 0
    i = 0
    for j in lines:
        start = i
        end = start+j
        if (end > size):
##            print start,end-size-1,end
            temp = a[start:size+1]
            temp = temp+a[0:end-size-1]
##            print temp
            temp = list(reversed(temp))
            a[start:size+1] = temp[0:size+1-start]
            a[0:end-size-1] = temp[size+1-start:]
        else:
            a[i:j] = list(reversed(a[i:j]))
        sk+=1
        i += sk+j
        while i > size:
            i-=size+1
    print a,a[0]*a[1]
    #The answer is not correct for the real question
