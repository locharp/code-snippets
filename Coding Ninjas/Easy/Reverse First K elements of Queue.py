def f( q, k ):

    if k < 1:
        return

    p = q.get()
    f( q, k - 1 )
    q.put( p )



def reverseElements( q, k ):
    
    f( q, k )

    for i in range( q.qsize() - k ):
        q.put( q.get() )

    return q
