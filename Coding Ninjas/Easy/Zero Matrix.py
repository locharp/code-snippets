def zeroMatrix( matrix, n, m ):
    
    for i in range( n ):
        t = False

        for j in range( m ):
            if matrix[i][j] == 0:
                t = True
                matrix[0][j] = 0

        if t:
            for j in range( m ):
                matrix[i][j] = 0

    for j in range( m ):
        if matrix[0][j] == 0:
            for i in range( 1, n ):
                matrix[i][j] = 0

    return matrix
