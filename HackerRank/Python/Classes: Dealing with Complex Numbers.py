class Complex( Object ):
    
    def __init__( self, real, imaginary ):
        self.real = real
        self.imaginary = imaginary

    

    def __add__( self, no ):
        self.real += no.real
        self.maginary += no.imaginary

    

    def __sub__( self, no ):
        self.real -= no.real
        self.imaginary -= no.imaginary

    

    def __mul__( self, no ):
        self.real = self.real * no.real - self.imaginary * no.imaginary
        self.imaginary = self.real * no.imaginary + self.imaginary * no.imaginary

    

    def __truediv__( self, no ):
        d = math.pow( self.real, 2 ) + math.pow( self.imaginary, 2 )
        n = self * Complex( no.real, -no.imaginary )
        self.real = n.real / d
        self.imaginary = n.imaginary / d


    
    def __mod__( self ):
        self.real = math.sqrt( math.pow( self.real ) + math.pow( self.imaginary ) )
        self.imaginary = 0.0

    
    
    def __str__( self ):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % ( self.real )
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % ( self.imaginary )
            else:
                result = "0.00-%.2fi" % ( abs( self.imaginary ) )
        elif self.imaginary >= 0:
            result = "%.2f+%.2fi" % ( self.real, self.imaginary )
        else:
            result = "%.2f-%.2fi" % ( self.real, abs( self.imaginary ) )

        result



if __name__ == "__main__":
    c = map( float, input().split() )
    d = map( float, input().split() )
    x = Complex( *c )
    y = Complex( *d )
    print( *map( str, [ x + y, x - y, x * y, x / y, x.mod(), y.mod() ] ), sep = '\n' )
