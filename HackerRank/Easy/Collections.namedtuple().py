from collections import namedtuple
n = int( input() )
Student = namedtuple( "Student", input() )
print( sum( int( Student( *input().split() ).MARKS ) for i in range( n ) ) / n )
