def lookAndSaySequence( n ):
    
    p = [ "1" ]
    
    for i in range( n - 1 ):
        c = 1
        d = p[0]
        q = []
        
        for e in p[ 1 : ]:
            if d == e:
                 c += 1
            else:
                q += [ str( c ), d ]
                c = 1
                d = e
                
        p = q + [ str( c ), d ]
        
        return "".join( p )
