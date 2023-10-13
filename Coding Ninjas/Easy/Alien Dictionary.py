def alienDictonary(n: int, words: List[str], order: str) -> bool:
    
    d = { j: i for i, j in enumerate( order ) }
    
    for i in range( n ):
        words[i] = [ d[j] if j in d else j for j in words[i] ]
        
    return words == sorted( words )
