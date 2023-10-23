def nb_year( p0, percent, aug, p ):
    ans = 0
    
    while p0 < p:
        p0 = p0 * percent // 100 + p0 + aug
        ans += 1
        
    return ans