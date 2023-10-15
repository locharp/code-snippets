def infixToPostfix( exp: str ) -> str:
    
    a, ans = [], []
    i = 0
    
    while i < len( exp ):
        if exp[i] == "^":
            while len( a ) > 0 and a[-1] == "^":
                ans.append( a.pop() )
                
            a.append( exp[i] )
        elif exp[i] in "*/":
            while len( a ) > 0 and a[-1] in "*/^":
                ans.append( a.pop() )
                
            a.append( exp[i] )
        elif exp[i] in"+-":
            while len( a ) > 0 and a[-1] != "(":
                ans.append( a.pop() )
                
            a.append( exp[i] )
        elif exp[i] == "(":
            a.append( exp[i] )
        elif exp[i] == ")":
            while len( a ) > 0:
                j = a.pop()
                
                if j == "(":
                    break
                else:
                    ans.append( j )
        else:
            ans.append( exp[i] )
            
        i += 1
    
    ans += a[ : : -1 ]
    
    return "".join( ans )
