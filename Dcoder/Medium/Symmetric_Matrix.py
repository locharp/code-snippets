n = int( input() )
matrix = []
for i in range( n ):
    matrix.append( input().split() )
  
for i in range( 1, n - 1 ):
    for j in range( i, n ):
        if matrix[i][j] != matrix[j][i]:
            print( "NO" )
            break
    else:
        continue
    
    break
else:
    print( "YES" )