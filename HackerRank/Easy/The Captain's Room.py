from collections import Counter

input()
ans = [ i for i, j in Counter( input().split() ).items() if j < 2 ]

print( ans[0] )
