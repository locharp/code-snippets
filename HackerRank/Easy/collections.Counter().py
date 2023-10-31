from collections import Counter

input()
c = Counter( map( int, input.split() ) )
ans = 0
for i in range( int( input() ) ):
    m, n = map( int, input().split() )
   
    if m in c and c[m] > 0:
        c[m] -= 1
        ans += n
       
print( ans )
