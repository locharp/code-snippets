def DNA_strand( dna ):
    ans = ""
    
    for ch in dna:
        if ch == "A":
            ans += "T"
        elif ch == "C":
            ans += "G"
        elif ch == "G":
            ans += "C"
        else:
            ans += "A"
            
    return ans