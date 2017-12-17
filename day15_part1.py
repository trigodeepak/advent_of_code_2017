n = 679
m = 771
mul_a = 16807
mul_b = 48271
modulus = 2147483647
res = 0
for i in xrange(40000001):
    if i % 10000000 == 0:
        print i
    n = (n * mul_a)%modulus
    m = (m * mul_b)%modulus
    a = format(int("{0:b}".format(n)),'032d')
    b = format(int("{0:b}".format(m)),'032d')
    if a[16:] == b[16:]:
        res+=1
print res
#This is very inefficient taken 10 mins to give the result
