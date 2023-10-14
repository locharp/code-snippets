class Complex( Object ):
    
    def __init__( self, real, imaginary ):
        self.real = real
        self.imaginary = imaginary

    

    def __add__( self, no ):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        
        return Complex( real, imarginary )
        
    

    def __sub__( self, no ):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        
        return Complex( real, imaginary )
        
    

    def __mul__( self, no ):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        
        return Complex( real, imaginary )
        
    

    def __truediv__( self, no ):
        r = Complex( no.real, -no.imaginary )
        d = ( no * r ).real
        n = self * r
        real = n.real / d
        imaginary = n.imaginary / d

        return Complex( real, imaginary )



    
    def __mod__( self ):
        real = math.sqrt( math.pow( self.real, 2 ) + math.pow( self.imaginary, 2 ) )
        imaginary = 0.0

        return Complex( real, imarginary )

    
    
    def __str__( self ):
        result = ""
        
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

        return result



if __name__ == "__main__":
    c = map( float, input().split() )
    d = map( float, input().split() )
    x = Complex( *c )
    y = Complex( *d )
    print( *map( str, [ x + y, x - y, x * y, x / y, x.mod(), y.mod() ] ), sep = '\n' )
