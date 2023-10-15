def infixToPostfix( exp: str ) -> str:
    
    a, ans = [], []
    i = 0
    
    for i in exp:
        if i == "^":
            while len( a ) > 0 and a[-1] == "^":
                ans.append( a.pop() )
                
            a.append( i )
        elif i in "*/":
            while len( a ) > 0 and a[-1] in "*/^":
                ans.append( a.pop() )
                
            a.append( i )
        elif i in"+-":
            while len( a ) > 0 and a[-1] != "(":
                ans.append( a.pop() )
                
            a.append( i )
        elif i == "(":
            a.append( i )
        elif i == ")":
            while len( a ) > 0:
                j = a.pop()
                
                if j == "(":
                    break
                else:
                    ans.append( j )
        else:
            ans.append( i )
            
    ans += a[ : : -1 ]
    
    return "".join( ans )
