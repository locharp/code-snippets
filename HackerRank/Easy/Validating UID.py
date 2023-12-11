import re

p = [ re.compile( r"[A-Za-z0-9]{10}" ), re.compile( r"^(?!.*(.).*\1)" ), re.compile( r"([A-Z].*){2,}" ), re.compile( r"([0-9].*){3,}" ) ]

for i in range( int( input() ) ):
    s = input()
    t = True
    
    for j in p:
        if j.search( s ) == None:
            print( "Invalid" )
            t = False
            break
            
    if t:
        print( "Valid" )
