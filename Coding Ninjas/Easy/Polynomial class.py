class Polynomial:
    
    def __init__( self, coeff = None ):

        if coeff is not None:
            self.degCoeff = [ i for i in coeff ]
        else:
            self.degCoeff = []


    
    def setCoefficient( self, d, c ):

        if len( self.degCoeff ) <= d:
            self.degCoeff += [ 0 ] * ( d - len( self.degCoeff ) + 2 )

        self.degCoeff[d] = c



    def __add__( self, other ):

        ans = Polynomial( self.degCoeff )

        while len( ans.degCoeff ) < len( other.degCoeff ):
            ans.degCoeff.append( 0 )
        
        for i in range( len( other.degCoeff ) ):
            ans.degCoeff[i] += other.degCoeff[i]

        return ans
        


    def __sub__( self, other ):
        
        ans = Polynomial( self.degCoeff )

        while len( ans.degCoeff ) < len( other.degCoeff ):
            ans.degCoeff.append( 0 )
        
        for i in range( len( other.degCoeff ) ):
            ans.degCoeff[i] -= other.degCoeff[i]

        return ans



    def __mul__( self, other ):

        m = len( self.degCoeff )
        n = len( other.degCoeff )
        ans = Polynomial()
        ans.degCoeff = [ 0 ] * ( m + n - 1 )
        
        for i in range( m ):
            for j in range( n ):
                ans.degCoeff[ i + j ] += self.degCoeff[i] * other.degCoeff[j]
        
        return ans



    def __eq__( self, other ):

        self.degCoeff = [ i for i in other.degCoeff ]



    def print( self ):
        
        while len( self.degCoeff ) > 0 and self.degCoeff[-1] == 0:
            self.degCoeff.pop()

        for i in range( len( self.degCoeff ) ):
            if self.degCoeff[i] != 0:
                print( str( self.degCoeff[i] ) + "x" + str( i ), end = " " )
