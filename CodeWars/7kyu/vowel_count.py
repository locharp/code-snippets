def get_count( sentence ):
    ans = 0
    
    for ch in sentence:
        if ch in "aeiou":
            ans += 1
            
    return ans