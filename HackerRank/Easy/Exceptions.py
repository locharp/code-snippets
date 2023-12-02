for i in range( int( input() ) ):
    try:
        a, b = map( int, input().split() )
        print( a // b )
    except ValueError as error:
        print( "Error Code:", error )
    except ZeroDivisionError:
        print( "Error Code: integer division or modulo by zero", )
