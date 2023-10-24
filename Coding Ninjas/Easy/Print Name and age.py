name = input()
age = input()

print( "The name of the person is {} and the age is {}.".format( name, age ) )





# OOP
class Person:

    def __init__( self, name, age ):

        self.SetValue( name, age )



    def SetValue( self, name, age ):

        self.__name = name
        self.__age = int( age )

        

    def GetValue( self ):
        
        print( "The name of the person is " + self.__name + " and the age is " + str( self.__age ) + "." )





person = Person( input(), input() )
person.GetValue()
