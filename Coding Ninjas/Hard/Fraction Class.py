from math import *

class Fraction:
    
    def __init__( self, numerator, denominator ):

        self.numerator = numerator
        self.denominator = denominator



    def add( self, other ):

        self.numerator = ( self.numerator * other.denominator ) + ( self.denominator * other.numerator )
        self.denominator *= other.denominator
        self.simplify()



    def multiply( self, other ):

        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.simplify()

    

    def simplify( self ):

        x = gcd( self.numerator, self.denominator )
        self.numerator //= x
        self.denominator //= x



    def print( self ):

        print( str( self.numerator ) + "/" + str( self.denominator ) )





n, d = map( int, input().split() )
f1 = Fraction( n, d )
N = int( input() )

for i in range( N ):
    o, n, d = map( int, input().split() )
    f2 = Fraction( n, d )

    if o == 1:
        f1.add( f2 )
        f1.print()
    elif o == 2:
        f1.multiply( f2 )
        f1.print()
