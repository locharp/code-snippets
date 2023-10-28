class Car:

    def __init__( self, noOfGear, color ):
        
        self.noOfGear = noOfGear
        self.color = color



    def printCarInfo( self ):

        print( "noOfGear:", self.noOfGear )
        print( "color:", self.color )
        


class RaceCar( Car ):
    
    def __init__( self, noOfGear, color, maxSpeed ):

        super().__init__( noOfGear, color )
        self.maxSpeed = maxSpeed
