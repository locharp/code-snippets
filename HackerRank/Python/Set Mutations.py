input()
a = set( map( int, input().split() ) )
n = int( input() )

for i in range( n ):
    operation = input().split()[0]
    another_set = map( int, input().split() )
    
    if operation == "update":
        a.update( another_set )
    elif operation == "intersection_update":
        a.intersection_update( another_set )
    elif operation == "difference_update":
        a.difference_update( another_set )
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update( another_set )
        
print( sum( a ) )
