def stringMania( n : int, m : int, str1 : str, str2 : str ) -> int:
    if str1 > str2:
        return 1
    elif str2 > str1:
        return -1
    else:
        return 0
