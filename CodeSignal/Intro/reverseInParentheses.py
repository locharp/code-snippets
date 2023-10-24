def solution( inputString ):
    p = []
    i = 0
  
    while i < len( inputString ):
        if inputString[i] == "(":
            p.append( i )
        elif inputString[i] == ")":
            inputString = inputString[ : p[ -1 ] ] + inputString[ i - 1 : p.pop() : -1 ] + inputString[ i + 1 : ]
            i -= 2
            
        i += 1
            
    return inputString
