def maxArea( height ):
    ans = m = 0
    n = len( height ) - 1
    
    while m < n:
        ans = max( min( height[m], height[n] ) * ( n - m ), ans )
        
        if height[m] > height[n]:
            n -= 1
        else:
            m += 1
            
    return ans
