from collections import namedtuple

n = int( input() )
Student = namedtuple( "Student", input() )
students = [ Student( *input().split() ) for i in range( n ) ]
print( "{:.2f}".format( sum( int( student.MARKS ) for student in students ) / n ) )
