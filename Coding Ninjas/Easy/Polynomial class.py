from copy import deepcopy

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

        p = self.degCoeff
        q = other.degCoeff
        
        if len( p ) < len( q ):
            p, q = q, p
        
        ans = Polynomial( p )

        for i in range( len( q ) ):
            ans.degCoeff[i] += q[i]

        return ans
        


    def __sub__( self, other ):

        p = self.degCoeff
        q = other.degCoeff
        
        if len( p ) < len( q ):
            p, q = q, p
        
        ans = Polynomial( p )

        for i in range( len( q ) ):
            ans.degCoeff[i] -= q[i]

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



def run():
    count1 = int(input())

    degree1 = list(map(int,input().split()))

    coeff1 = list(map(int,input().split()))


    first = Polynomial()
    for i in range(count1):
        first.setCoefficient(degree1[i], coeff1[i])

    count2 = int(input())


    degree2 = list(map(int,input().split()))

    coeff2 = list(map(int,input().split()))


    second = Polynomial()
    for i in range(count2) :
        second.setCoefficient(degree2[i], coeff2[i])


    choice = int(input())

    result = Polynomial()
    # Add 
    if choice == 1:
        result = first + second
        result.print()
    # Subtract
    elif choice == 2:
        result = first - second
        result.print()
    # Multiply
    elif choice == 3:
        result = first * second
        result.print()

    elif choice == 4: # Copy constructor
        third = deepcopy(first)
        if (third.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")

    else: # Copy assignment operator
        fourth = deepcopy(first)
        if (fourth.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")



run()
