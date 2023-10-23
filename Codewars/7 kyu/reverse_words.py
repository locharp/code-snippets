def reverse_words( text ):
    ans = ""
    i = 0
    
    for j in range( len( text ) ):
        if text[j] == " ":
            ans += text[ i : j ][ : : -1 ] + " "
            i = j + 1
            
    ans += text[ i : ][ : : -1 ]
    
    return ans