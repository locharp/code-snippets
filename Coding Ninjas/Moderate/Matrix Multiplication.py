def multiplyMatrices( mat1, mat2 ):
    
    return [ [ sum( mat1[i][k] * mat2[k][j] for k in range( len( mat2 ) ) ) for j in range( len( mat2[0] ) ) ] for i in range( len( mat1 ) ) ]
