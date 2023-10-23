from textwrap import wrap

def rev_rot( strng, sz ):
    
    if sz < 1 or sz > len( strng ):
        return ""
    elif sz < 2 or len( strng ) < 2:
        return strng
    
    a = wrap( strng, sz )
    
    if len( a[-1] ) < sz:
        a.pop()
    
    for i in range( len( a ) ):
        if sum( j ** 3 for j in tuple( map( int, a[i] ) ) ) % 2 == 0:
            a[i] = a[i][ : : -1 ]
        else:
            a[i] = a[i][ 1 : ] + a[i][0]
            
    return "".join( a )            
