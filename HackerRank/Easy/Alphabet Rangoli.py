from string import ascii_lowercase

def print_rangoli( size ):
    
    rangoli = []
    
    for i in range( 1, size + 1 ):
        s = [ ascii_lowercase[j] for j in range( size - i, size ) ]
        s = "-".join ( s[ : 0 : -1 ] + s )
        
        rangoli.append( s.center( size * 4 - 3, "-" ) )
        print( rangoli[-1] )
    
    for i in range( size - 2, -1, -1 ):
        print( rangoli[i] )
