class Shape:

    def printMyType( self ):

        print( self.shapeType )





class Square( Shape ):

    def __init__( self, length ):
        
        self.shapeType = "square"
        self.length = length



    def  calculateArea( self ):

        return self.length * self.length
        




class Rectangle( Shape ):

    def __init__( self, length, breadth ):

        self.shapeType = "rectangle"
        self.length = length
        self.breadth = breadth if breadth > 0 else length



    def  calculateArea( self ):

        return self.length * self.breadth





square = Square( 5 )
square.printMyType()
print( square.calculateArea() )

rectangel = Rectangle( 5, 4 )
rectangel.printMyType()
print( rectangel.calculateArea() )
