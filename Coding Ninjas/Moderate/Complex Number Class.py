class ComplexNumbers:
    
    def __init__( self, real, imaginary ):

        self.real = real
        self.imaginary = imaginary



    def plus( self, other ):

        self.real += other.real
        self.imaginary += other.imaginary

        return ( self.real, self.imaginary )

    
    
    def multiply( self, other ):

        real = ( self.real * other.real ) - ( self.imaginary * other.imaginary )
        self.imaginary = ( self.real * other.imaginary ) + ( self.imaginary * other.real )
        self.real = real
        
        return ( self.real, self.imaginary )
    
    

    def print( self ):

        print( str( self.real ) + " + i" + str( self.imaginary ) )





r, i = map( int, input().split() )
c1 = ComplexNumbers( r, i )
r, i = map( int, input().split() )
c2 = ComplexNumbers( r, i )
o = int( input() )

if o == 1:
    c1.plus( c2 )
    c1.print()
elif o == 2:
    c1.multiply( c2 )
    c1.print()
