s = input()
n = len( s )

if n % 2 == 1:
    print( "No" )
elif n == 0 or s.count("(") == len( s ) // 2:
    print( "Yes" )
else:
    print( "No" )