def remove_url_anchor( url ):
    ans = ""
    
    for ch in url:
        if ch == "#":
            break
            
        ans += ch
        
    return ans
