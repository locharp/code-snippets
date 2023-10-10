from functools import reduce

def productPuzzle( arr ):
    
    return [ reduce( mul, arr[ : i ] + arr[ i + 1 : ] ) % ( 10 ** 9 + 7 ) for i in range( len( arr ) ) ] 
