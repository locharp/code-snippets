def f( m, a, o ):
        
        if len( m ) < 1:
            return a
        
        s = set()
        
        for n in m:
            if n.left is None:
                if n.right is None:
                    a.add( o )
                else:
                    s.add( n.right )
            else:
                s.add( n.left )
                
                if n.right is not None:
                    s.add( n.right )
            
        return f( s, a, o + 1 )
    
    

def levelLeaf( root: Node )-> int:

    a = f( [ root ], set(), 0 )
    
    return 0 if len( a ) > 1 else 1
