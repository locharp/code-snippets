def setZeros( matrix: List[ List[int] ] ) -> None:
    n = len( matrix )
    m = len( matrix[0] )
    p = set()
    q = set()
    
    for i in range( n ):
        for j in range( m ):
            if matrix[i][j] == 0:
                p.add( i )
                q.add( j )
                
    for i in range( n ):
        if i in p:
            for j in range( m ):
                matrix[i][j] = 0
        else:
            for j in q:
                matrix[i][j] = 0