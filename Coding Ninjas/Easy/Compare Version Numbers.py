def compareVersions( a, b ):
    
    u = a.split( "." )
    v = b.split( "." )
    i = 0
    m = min( len( u ), len( v) )

    while i < m:
        if int( u[i] ) > int( v[i] ):
            return 1
        elif int( v[i] ) > int( u[i] ):
            return -1

        i += 1

    while i < len( u ):
        if u[i] != "0":
            return 1

        i += 1

    while i < len( v ):
        if v[i] != "0":
            return -1

        i += 1
    
    return 0
