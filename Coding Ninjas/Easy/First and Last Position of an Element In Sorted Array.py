def firstAndLastPosition(arr, n, k):

    i = 0

    while i < n and arr[i] < k:
        i += 1

    if i == n or arr[i] > k:
        return [ -1, -1 ]
    
    j = i + 1

    while j < n and arr[j] == k:
        j += 1

    return [ i, j - 1 ]
