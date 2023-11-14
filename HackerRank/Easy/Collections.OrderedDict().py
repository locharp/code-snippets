from collections import OrderedDict

d = OrderedDict()

for i in range( int( input() ) ):
    a = input().split()
    p = " ".join( a[ : -1 ] )
    q = int( a[-1] )
    
    if p not in d:
        d[p] = 0
    
    d[p] += q
    
for i, j in d.items():
    print( i, j )
