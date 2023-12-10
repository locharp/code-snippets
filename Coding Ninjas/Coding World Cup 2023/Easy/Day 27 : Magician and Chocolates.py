from bisect import bisect_right

def maximumChocolates(arr, k):
    arr.sort()
    ate = 0
    mod = int(1E9 + 7)
    
    for i in range(k):
        eat = arr.pop()
        ate = (ate + eat) % mod
        refill = eat // 2
        arr.insert(bisect_right(arr, refill), refill)

    return ate
