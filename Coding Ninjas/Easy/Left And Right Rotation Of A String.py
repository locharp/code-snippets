def leftRotate( strr, d ):

    d %= len( strr )
    
    return strr[ d : ] + strr[ : d ]



def rightRotate(strr, d):
    
    d %= len( strr )
    
    return strr[ -d : ] + strr[ : -d ]
