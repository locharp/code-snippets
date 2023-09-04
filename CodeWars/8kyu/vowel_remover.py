def shortcut( s ):
    ans = ""
    
    for ch in s:
        if ch not in "aeiou":
            ans += ch
            
    return ans