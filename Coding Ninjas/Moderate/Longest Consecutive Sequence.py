from sortedcontainers import SortedSet

def lengthOfLongestConsecutiveSequence( arr, n ):
    
    s = SortedSet( arr )
    ans = 1
    a = s[0]
    c = 1

    for i in s:
        if i == a + 1:
            c += 1
            ans = max( ans, c )
        else:
            c = 1

        a = i

    return ans
