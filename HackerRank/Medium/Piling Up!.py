for i in range( int( input() ) ):
    input()
    a = list( map( int, input().split() ) )
    
    curr = 2 ** 31 + 1
    t = True
    
    while len( a ) > 0:
        if a[0] > a[-1]:
            if a[0] <= curr:
                curr = a.pop( 0 )
            else:
                t = False
                break
        elif a[-1] <= curr:
            curr = a.pop()
        else:
            t = False
            break
            
    if t:
        print( "Yes" )
    else:
        print( "No" )
