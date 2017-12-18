n = 328
s = [0,1]
ind = 1
val = 2
while (val<=2017):
    ind += n
    ind = ind%val
    ind +=1
    s.insert(ind,val)
    val+=1
print s[s.index(2017)+1]
