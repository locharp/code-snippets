from collections import Counter

input()
c = Counter( input().split() )
ans = 0

for i in range( int( input() ) ):
    j, k = input().split()
    
    if j in c and c[j] > 0:
        c[j] -= 1
        ans += int( k )
        
print( ans )
