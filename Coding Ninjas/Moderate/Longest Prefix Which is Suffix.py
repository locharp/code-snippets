def longestPrefixSuffix( str: str ) -> str:
    for i in range( len( str ) - 1, 0, -1 ):
        if str[ : i ] == str[ -i : ]:
            return str[ : i ]
        
    return ""