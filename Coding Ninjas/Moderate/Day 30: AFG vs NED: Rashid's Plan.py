def countEvenParityDigits( a: str ) -> int:

    return len( [ i for i in a if int( i ) % 2 == 0 ] )
