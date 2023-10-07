input()
s = set( map( int, input().split() ) )
n = int( input() )

for i in range( n ):
    command = input().split()

    if command[0] == "remove":
        s.remove( int( command[1] ) )
    elif command[0] == "discard":
        s.discard( int( command[1] ) )
    elif command[0] == "pop":
        s.pop()

print( sum( s ) )
