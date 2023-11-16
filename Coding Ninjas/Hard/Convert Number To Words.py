def handleAll( n ):
    
    a = []
    c = [ "", "one", "two", "three" ,"four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "", ]
    d = [ "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    e = [ "", "", "hundred", "thousand", "", "lakh", "", "crore", "" ]
    ans = []
    
    while n > 0:
        a.append( n % 10 )
        n //= 10
        
    for i in range( len( a ) ):
        if e[i] != "":
            ans.append( e[i] )
        
        if ( i == 0 or i > 2 and ( i - 3 ) % 2 == 0 ) and i + 1 < len( a ) and a[ i + 1 ] == 1:
                ans.append( c[ a[i] + 10 ] )
                a[ i + 1 ] = 0
        elif i == 1 or i > 3 and ( i - 3 ) % 2 == 1:
            if d[ a[i] ] != "":
                ans.append( d[ a[i] ] )
        else:
            if c[ a[i] ]:
                ans.append( c[ a[i] ] )
            
        if i == 1 and len( ans ) > 0:
            ans.append( "and" )
            
    i = 0
    
    while i < len( ans ):
        if ans[i] in e and i + 1 < len( ans ) and ans[ i + 1 ] in e:
            ans.pop( i )
        else:
            i += 1
         
    return " ".join( ans[ : : -1 ] )
