def sort012( arr, n ) :
    i = p = 0
    q = n - 1

    while i <= q:
        if p > i:
            i += 1
        elif arr[i] < 1:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
        elif arr[i] > 1:
            arr[i], arr[q] = arr[q], arr[i]
            q -= 1
        else:
            i += 1
