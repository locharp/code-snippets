def maxSubarraySum( arr, n ) :
    ans = 0
    curr = 0
    
    for i in arr:
        curr = max( 0, curr + i )
        ans = max( ans, curr )
        
    return ans
