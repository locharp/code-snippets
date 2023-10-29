def linearSearch( n: int, num: int, arr: [int] ) -> int:

    for i in range( n ):
        if num == arr[i]:
            return i

    return -1
