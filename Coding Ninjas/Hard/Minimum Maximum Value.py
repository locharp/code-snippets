from typing import Tuple

def minMaxValue( exp: str ) -> Tuple[ int, int ]:
    
    ans = [ float( "inf" ), 0 ]
    i, j = -1, 0
    c = []
    
    while j < len( exp ):
        if exp[j] == "+" or exp[j] == "*":
            c.append( [ exp[i], int( exp[ i + 1 : j ] ) ] )
            i = j
            
        j += 1
        
    c[0][0] = "+"
    d = [ [ [ i, j ] for i, j in c ] ]
    e = []
    i = 0
    
    while i < len( c ):
        if c[i][1] == 0:
            o = False
            q = i
            
            while q < len( c ) and c[q][1] == 0:
                if c[q][0] == "*":
                    o = True
                    
                q += 1
                
            if q < len( c ) and c[i][0] != "*" or c[q][0] != "*":
                if o:
                    c[q][0] = "*"
                    
                c = c[ : i ] + c[ q : ]
                continue
            elif q > i + 1:
                c = c [ : i + 1 ] + c[ q : ]
                
            m = n = 1
            p, q = i, i + 1
            
            while p > 0 and c[p][0] == "*":
                p -= 1
                m *= c[p][1]
                
            while q < len( c ) and c[q][0] == "*":
                n *= c[q][1]
                q += 1
                
            if m > n:
                c = c[ : i ] + c[ q : ]
            else:
                c = c[ : p ] + c[ i + 1 : ]
                i = p
                
        i += 1
        
    i = 1
    
    while i < len( c ):
        if c[i][0] == "+":
            c[ i - 1 ][1] += c.pop( i )[1]
        else:
            i += 1
            
    if len( c ) > 0:
        ans[1] = 1
        
        for i in c:
            ans[1] *= i[1]
            
    while len( d ) > 0:
        f = d.pop()
        i = 0
        
        while i < len( f ):
            if f[i][1] == 0:
                if i + 1 < len( f ) and f[ i + 1 ][1] == 0:
                    d.append( f[ : i + 1 ] )
                    d.append( f[ i + 1 : ] )
                    break
                    
                m = n =1
                p = 0 if f[i][0] == "*" else i
                q = i + 1
                
                if q < len( f ) and f[q][0] == "*":
                    q = len(f)
                    
                f = f[ : p ] + f[ q : ]
                i = p
                
            i += 1
            
        e.append( f )
        
    for f in e:
        i = 1
        
        while i < len( f ):
            if f[i][0] == "*":
                f[ i - 1 ][1] *= f.pop( i )[1]
            else:
                i += 1
                
    for f in e:
        ans[0] = min( ans[0], sum( i[1] for i in f ) )
        
    return ans
